
def sip_calculator(monthly_amount, roi, frequency, time):
    # frequency : months in year

    roi = roi / (100 * frequency) # convert annual rate of return to rate per period
    frequency = frequency * time # convert the number of compounding periods to the total number of periods
    maturity_amount = monthly_amount * (((1 + roi) ** frequency - 1) / roi) * (1 + roi)
    invested_amount = monthly_amount * frequency * time
    return [round(maturity_amount, 2), invested_amount]

monthly_investment = 20000
annual_rate_of_return = 12
compounding_frequency = 12
investment_duration_in_years = 10
for x in range(compounding_frequency):
    print(monthly_investment+(1000*x))


maturity_amount = sip_calculator(monthly_investment, annual_rate_of_return, compounding_frequency, investment_duration_in_years)

print(f"The maturity amount for a SIP investment of Rs. {monthly_investment} per month for {investment_duration_in_years} years at an annual rate of return of {annual_rate_of_return}% is Rs. {maturity_amount[0]}. with investment of Rs. {maturity_amount[1]}")

