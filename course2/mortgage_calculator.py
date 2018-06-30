class MortgageCalculator:
    __interest_rate = 0.036
    __principal_pay = 200000
    __total_value = 400000
    __terms_year = 25

    def __init__(self, interest_rate, principal_pay, total_value, terms_year):
        self.__interest_rate = interest_rate
        self.__principal_pay = principal_pay
        self.__total_value = total_value
        self.__terms_year = terms_year
        self.__terms_month = terms_year * 12

    def get_interest_rate(self):
        return self.__interest_rate

    def __str__(self):
        return "Interest_rate: %s\nPrincipal Pay: %d\n" % (self.__interest_rate, self.__principal_pay)

    def calculator(self):
        interest_low_month = self.__interest_rate / 12
        mortgage = self.__total_value - self.__principal_pay
        total_payment = (self.__total_value - self.__principal_pay) * ((1 + interest_low_month) ** self.__terms_month)
        # if we use the low interest loan, we planing to equal payment in the next 25 years
        # and we using monthly pay
        # Term 1: a, a*(1+interest_low)**(terms_month -1)
        # Term 2: a, a*(1+interest_low)**(terms_month -2)
        # total_value/terms_month< a < 10*total_value/terms_month
        principal = 0
        base_principal = mortgage // self.__terms_month

        def seq(start, stop, step=1):
            n = int(round((stop - start) / float(step)))
            if n > 1:
                return ([start + step * i for i in range(n + 1)])
            elif n == 1:
                return ([start])
            else:
                return ([])

        for a in seq(base_principal, 10 * mortgage // self.__terms_month, 0.01):
            total_paid = 0
            for term in range(0, self.__terms_month):
                total_paid += a * ((1 + interest_low_month) ** (self.__terms_month - term))
            if total_payment - total_paid < total_payment * 0.000000001:
                print(a, total_paid, total_payment)
                principal = a
                break

        for term in range(self.__terms_month):
            print("Term %d: \nPrincipal: %f,Interests:%f, Total:%f  "
                  % (term, principal, principal * ((1 + interest_low_month) ** (self.__terms_month - term) - 1),
                     principal * (1 + interest_low_month) ** (self.__terms_month - term)))

        print('Total paid:%f,Amortization Interest Cost:%f' %
              (principal * self.__terms_month, principal * self.__terms_month - mortgage))
        return principal, principal * self.__terms_month - mortgage

    def cash_back(self, amount):
        return amount * ((1 + self.__interest_rate) ** self.__terms_year)

    def cash_back_difference(self,new_rate,amount):
        difference=0
        return difference

if __name__ == "__main__":
    print('''
    Purchase Price:400,000
    Down payment: 200,000
    Interests rateL: 3.74%
    Terms: 25 years
    Monthly payment: ???
    
    ''')
    plan_a = MortgageCalculator(0.037, 200000, 400000, 25)
    plan_b = MortgageCalculator(0.035, 200000, 400000, 25)

    print(plan_a)
    print(plan_a.cash_back(1000))

    print(plan_b)

    # print(plan_a.calculator())

    print(plan_b.cash_back(1000))
    print(plan_b.get_interest_rate())

    plan_c = MortgageCalculator(interest_rate=0.035, principal_pay=300000, total_value=400000, terms_year=25)
    print(plan_c.calculator())
