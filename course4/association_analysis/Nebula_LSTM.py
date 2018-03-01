import threading

from sklearn.preprocessing import MinMaxScaler
from collections import deque
from matplotlib import pyplot
from keras import models
from keras import layers
import pandas as pd
import numpy as np
import time
import json
import datetime
import os
import matplotlib.pylab as plt
import requests
import time


def data_handler(end_time):
    FETCH_URL = "https://poloniex.com/public?command=returnChartData&currencyPair=%s&start=%d&end=%d&period=900"

    # unix timestamp
    start_time = end_time - 9999

    url = FETCH_URL % ("USDT_ETH", start_time, end_time)
    response = requests.get(url)
    response_text = response.text

    return response_text

def grouped(data_scaled, pin, pout, dropnan=True):
    vrs = 1 if type(data_scaled) is list else data_scaled.shape[1]
    df = pd.DataFrame(data_scaled)
    group = list()
    title = list()
    for i in range(pin, 0, -1):
        group.append(df.shift(i))
        title += [('various%d(t-%d)' % (j + 1, i)) for j in range(vrs)]
    for i in range(0, pout):
        group.append(df.shift(-i))
        if i == 0:
            title += [('various%d(t)' % (j + 1)) for j in range(vrs)]
        else:
            title += [('various%d(t+%d)' % (j + 1, i)) for j in range(vrs)]
    collect = pd.concat(group, axis=1)
    collect.columns = title
    if dropnan == True:
        collect.dropna(inplace=True)
    return collect


def difference(dataset, interval=1):
    diff = list()
    for i in range(interval, len(dataset)):
        value = dataset[i] - dataset[i - interval]
        diff.append(value)
    return pd.Series(diff)


# data cleaning, transform
def data_handling(data_raw, point_test, point_in, point_out):
    raw_data = data_raw.values
    different_rawdata = difference(raw_data, 1)
    different_values = different_rawdata.values
    different_values = different_values.reshape(len(different_values), 1)
    limitator = MinMaxScaler(feature_range=(-1, 1))
    data_scaled = limitator.fit_transform(different_values)
    data_scaled = data_scaled.reshape(len(data_scaled), 1)
    group = grouped(data_scaled, point_in, point_out)
    group_arr = group.values
    lst1 = group_arr[-1]
    list_deque = deque(lst1)
    for i in range(point_out):
        list_deque.rotate(-1)
        lst = np.array(list_deque)
        group_arr = np.append(group_arr, [lst], axis=0)
    team_train, team_test = group_arr[0:-point_test], group_arr[-point_test:]
    return limitator, team_train, team_test




# fit model, simple layers
def model_fit(data_train, point_in, batch, epochs, units):
    input = data_train[:, 0:point_in]
    output = data_train[:, point_in:]
    input = input.reshape(input.shape[0], 1, input.shape[1])
    model = models.Sequential()
    model.add(layers.LSTM(units, batch_input_shape=(batch, input.shape[1], input.shape[2]), stateful=True))
    # model.add(layers.LSTM(units=1, input_shape=data_train, return_sequences=False))
    model.add(layers.Dense(output.shape[1]))
    model.compile(loss='mse', optimizer='adam')
    for i in range(epochs):
        model.fit(input, output, epochs=1, batch_size=batch, verbose=0, shuffle=False)
        model.reset_states()
    return model


def lstm(model, input, batch):
    input = input.reshape(1, 1, len(input))
    predicts = model.predict(input, batch_size=batch)
    return [x for x in predicts[0, :]]


# predict via lstm model
def predicts(model, batch, data_test, point_in):
    predicts = list()
    for i in range(len(data_test)):
        input = data_test[i, 0:point_in]
        prediction = lstm(model, input, batch)
        predicts.append(prediction)
    return predicts



# recover data
def inver_diff(lst_one, scale_inversed):
    inverted = list()
    inverted.append(scale_inversed[0] + lst_one)
    for i in range(1, len(scale_inversed)):
        inverted.append(scale_inversed[i] + inverted[i - 1])
    return inverted


# tansform data set into original state
def inverse(data_raw, prediction, limitator, pint_test):
    inverts = list()
    for i in range(len(prediction)):
        predicts = np.array(prediction[i])
        predicts = predicts.reshape(1, len(predicts))
        scale_inversed = limitator.inverse_transform(predicts)
        scale_inversed = scale_inversed[0, :]
        index = len(data_raw) - pint_test + i - 1
        lst_one = data_raw.values[index]
        inv_diff = inver_diff(lst_one, scale_inversed)
        inverts.append(inv_diff)
    return inverts


# # standard deviation
# def evaluation(test, prediction, point_out):
#     print("Predicted Result Evaluation:")
#     for i in range(point_out):
#         data_recorded = [row[i] for row in test]
#         predicted = [predict[i] for predict in prediction]
#         data_mean = np.mean(data_recorded)
#         for k in predicted:
#             predicted_sqr = (k - data_mean)**2
#             predicted_sqr += predicted_sqr
#         sd = predicted_sqr/len(data_recorded)
#         print('data point%d - SD is %f' % ((i + 1), sd))


# def plot_result(data_raw, prediction, point_out):
#     pyplot.plot(data_raw.values)
#     time_len = len(data_raw)
#     time_space = list(data_raw.index)
#     for i in range(len(prediction)):
#         start_point = len(data_raw) - point_out + i
#         end_point = start_point + len(prediction[i]) + 1
#         xaxis = [x for x in range(start_point, end_point)]
#         yaxis = [data_raw.values[start_point]] + prediction[i]
#         pyplot.xticks(np.arange(time_len), time_space, rotation='vertical')
#         pyplot.plot(xaxis, yaxis, 'g')
#     pyplot.show()


class GetRequest:
    def __init__(self, data_indicator):
        self.data_indicator = data_indicator

    def execute_pro(self):
        current_time = int(time.time())
        # five_minutes_before = current_time - 6 *300
        data_in_json = data_handler(current_time)
        data = pd.read_json(data_in_json, convert_dates=False)
        human_time = data['date']
        human_time = human_time.tolist()
        x, date = [], []
        for tm in human_time:
            date.append(datetime.datetime.fromtimestamp(tm).strftime('%Y-%m-%d %H:%M'))
        for i in range(len(human_time)):
            x.append(i)
        date = np.transpose(date)
        indicator_values = data[self.data_indicator].values
        indicator_values = indicator_values.flatten()
        d = {'date': date, self.data_indicator: indicator_values}
        data = pd.DataFrame(data=d, index=date)
        range_ts = 500
        start_index_ts = 0 - range_ts
        ts0 = data[self.data_indicator][start_index_ts:]
        # print(ts0)

        # main
        # data point intended
        point_in = 1
        # data point predicted
        point_out = 6
        # data point tested
        point_test = 1
        epochs = 100
        batch = 1
        units = 1
        data_raw = ts0
        # print(data_raw)
        # current_time = int(time.time())
        # data_in_json= data_request.data_handler(current_time)
        # data = pd.read_json(data_in_json,convert_dates=False)
        # assign training set and testing set
        limitator, data_train, data_test = data_handling(data_raw, point_test, point_in, point_out)
        # build model
        model = model_fit(data_train, point_in, batch, epochs, units)
        # prediction of difference
        prediction = predicts(model, batch, data_test, point_in)
        # return to raw
        prediction = inverse(data_raw, prediction, limitator, point_test + 2)
        # data_recorded = [row[point_in:] for row in data_test]
        data_recorded = [row[1:] for row in data_test]
        data_recorded = inverse(data_raw, data_recorded, limitator, point_test + 2)
        # evaluation(data_recorded, prediction, point_out)
        # plot_result(data_raw, prediction, point_test)
        # print(data_recorded)

        print(prediction)

        json_data = {
            "prediction":prediction
        }
        if not os.path.exists("json_outputs"):
            os.makedirs("json_outputs")

        return prediction


#  output multiple files
json_out_path = os.path.join("", "output.json")

keylist=['open','close','high','low']
with open(json_out_path, "w")as jsonfile:
    dic = {}
    for each_indicate in keylist:
        # json.dump({each_indicate: GetRequest(each_indicate).execute_pro()},jsonfile
        dic[each_indicate] = GetRequest(each_indicate).execute_pro()
    json.dump(dic, jsonfile)


        # data_in_json_test = data_request_eth.data_handler(current_time)
        # data_test = pd.read_json(data_in_json_test, convert_dates=False)
        # index_range_truets = 6
        # start_index_truets = 0 - index_range_truets
        # truets = data_test[self.data_indicator][start_index_truets:]
        # truets = np.array(truets)
        #
        # date_test = data_test['date'][start_index_truets:]
        # date_test = date_test.tolist()
        # mergedlist = np.append(data_raw, truets)
        # mergedlist2 = np.append(data_raw, prediction)
        # plt.plot(mergedlist2)
        # plt.plot(mergedlist)
        #
        # plt.show()



#
# if __name__=="__main__":
#
#     # GetRequest(str_tread name, num_delay_minutes)
#     threadopen = GetRequest('open').execute_pro()
#     threadclose = GetRequest('close').execute_pro()
#     threadhigh = GetRequest('high').execute_pro()
#     threadlow = GetRequest('low').execute_pro()
#
#     # runtime error and Tcl_AsyncDelete, caused by GUI image, can be ignored
