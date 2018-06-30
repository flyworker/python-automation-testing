interest_high = 0.045

principal_pay = 200000
total_value = 400000
terms_year = 25
terms_month = terms_year * 12


def mortgage_calculator(interest_rate=0.03):
    interest_low_month = interest_rate / 12
    mortgage = total_value - principal_pay
    total_payment = (total_value - principal_pay) * ((1 + interest_low_month) ** terms_month)
    # if we use the low interest loan, we planing to equal payment in the next 25 years
    # and we using monthly pay
    # Term 1: a, a*(1+interest_low)**(terms_month -1)
    # Term 2: a, a*(1+interest_low)**(terms_month -2)
    # total_value/terms_month< a < 10*total_value/terms_month
    principal = 0
    base_principal = mortgage // terms_month

    def seq(start, stop, step=1):
        n = int(round((stop - start) / float(step)))
        if n > 1:
            return ([start + step * i for i in range(n + 1)])
        elif n == 1:
            return ([start])
        else:
            return ([])

    for a in seq(base_principal, 10 * mortgage // terms_month, 0.01):
        total_paid = 0
        for term in range(0, terms_month):
            total_paid += a * ((1 + interest_low_month) ** (terms_month - term))
        if total_payment - total_paid < total_payment * 0.000000001:
            print(a, total_paid, total_payment)
            principal = a
            break

    for term in range(terms_month):
        print("Term %d: \nPrincipal: %f,Interests:%f, Total:%f  "
              % (term, principal, principal * ((1 + interest_low_month) ** (terms_month - term) - 1),
                 principal * (1 + interest_low_month) ** (terms_month - term)))

    print('Total paid:%f,Amortization Interest Cost:%f' %
          (principal * terms_month, principal * terms_month - mortgage))
    return principal, principal * terms_month - mortgage


if __name__ == "__main__":
    print('''
    Purchase Price:400,000
    Down payment: 200,000
    Interests rateL: 3.74%
    Terms: 25 years
    Monthly payment: ???
    
    ''')
    interest_rate_low = 0.0374
    interest_rate_high = 0.036

    principal_low, amortization_interest_cost_low = mortgage_calculator(interest_rate_low)
    principal_high, amortization_interest_cost_high = mortgage_calculator(interest_rate_high)

    print('Principal Difference: %f$,Amortization Interest Cost Difference:%f$'
          % (principal_high - principal_low, amortization_interest_cost_high - amortization_interest_cost_low))
    rebate_amount=2000
    rebate_after_term=2000* ((1 + 0.072) ** terms_year)
    income_tax=0.5
    print(rebate_after_term*income_tax)