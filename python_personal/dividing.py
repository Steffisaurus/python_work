# set prompt for user
prompt = "\nEnter a dividend to check if its divisible by the divisor entered!"
prompt += "\nOnce you're done enter 'quit' to end."

# set while loop 
while True:
    
    # print prompt ask for dividend and divisor, check for quit, convert to int
    print(prompt)
    dividend = input()
    if dividend == 'quit':
        break
    else:
        dividend = int(dividend)

    divisor = input()
    if divisor == 'quit':
        break
    else:
        divisor = int(divisor)

    # if dividend / divisor give answer otherwise ask for retry
    if dividend % divisor == 0:
        amount = dividend / divisor
        print(f"Your dividend {dividend} is divisible by {divisor} {amount} time(s)!")
    else:
        print(f"I'm sorry, {dividend} is not divisible by {divisor}. Please try again")

# changelog
# v.01
# created, dividing the given dividend by 7, telling you if it is divisible.
# v.02
# added another line, telling the user how often the dividend was divided by 7.
# v.03
# added a 2nd input allowing for the user to specify dividend and divisor.
# v.04
# made quitting the application easier