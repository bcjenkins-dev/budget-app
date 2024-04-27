import MoneyBags as mb
# accept user input for current amount in savings
# TODO: Data validation
curr_savings = input("Enter current amount in savings: ")

# Hey you... I love you :)

# accept user input for paycheck amount
# TODO: Data validation
curr_income = input("Enter current amount per paycheck: ")

# accept user input for paycheck frequency and pay day
# TODO: Data validation
pay_freq = input("Enter frequency pay is received (every 2 weeks = 2w): ")
pay_day = input("Enter day of week pay is received (M,T,W,Th,F,S,Su): ")

# collect users categories of needs
print("Below enter the different categories and amounts for your needs. Some categories to consider are: rent, auto, groceries, personal care, and pets.")

mb_arr = []
first = True
while True:
    if not first:
        chk = input("Enter another need (y/n): ")
        if chk == "n":
            break
    first = False
    category = input("Enter this need's category: ")
    amount,amt_freq,amt_freq_unit = input("Enter the amount spent, the frequency it is spent in (ex. 500 14 d): ").split()
    tmp_mb = mb.MoneyBags(category, amount, amt_freq, amt_freq_unit)
    mb_arr.append(tmp_mb)
    tmp_mb.getBag()