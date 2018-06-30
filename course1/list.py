a = {
    "quoteVolume": "425.9338696054",
    "baseVolume": "2596728.104756011839",
    "highestBid": "6136.6",
    "high24hr": "6176.47",
    "last": "6145.98",
    "lowestAsk": "6145.99",
    "elapsed": "10ms",
    "result": "true",
    "low24hr": "5935.38",
    "percentChange": "2.037096067259"
}

# if float(a['low24hr'])>6000:
#     print('I have profit')
# else:
#     print('No supper')

import random

b = random.randint(1, 21)
# count = 5
# while count > 0:
#     print(b)
#     if b > 10:
#         b = random.randint(1, 21)
#     else:
#         print('Found B, value is', b)
#         break
#     count = count - 1
#
# for x in range(20):
#     if (x == 5):
#         continue
#     print(x)

count=1
while True:
    if count<5:
        count=count+1
        while True:
            print('inner')
            break
    else: break
    print(count)