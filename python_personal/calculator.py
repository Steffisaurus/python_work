# set prompt for user
prompt = "\nPlease enter an arithmetic operation (+, -, *, /) "
prompt += "\nOnce you're done with this program enter 'quit' to end."

# print prompt to user
print(prompt)

# set history list for operations
history = []

# set while loop 
while True:
    
    # ask for number, check for quit, convert string to number
    number_0 = input("\nPlease enter the first number: ")
    if number_0.lower() == 'quit':
        break
    else:
        number_0 = int(number_0)
    
    #  ask for arithmetic symbol, check for quit
    symbol = input("Please enter an arithmetic symbol: ")
    if symbol.lower() == 'quit':
        break
    
    # ask for second number, check for quit, convert string to number
    number_1 = input("Please enter the second number: ")
    if number_1.lower() == 'quit':
        break
    else:
        number_1 = int(number_1)

    # if arithmetic symbol valid, get result, append operation to list
    if symbol == '+':
        result_final = number_0 + number_1
        result = f"{number_0} + {number_1} = {result_final}"
        history.append(result)
    elif symbol == '-':
        result_final = number_0 - number_1
        result = f"{number_0} - {number_1} = {result_final}"
        history.append(result)
    elif symbol == '*':
        result_final = number_0 * number_1
        result = f"{number_0} * {number_1} = {result_final}"
        history.append(result) 
    elif symbol == '/':
        result_final = number_0 / number_1
        result = f"{number_0} / {number_1} = {result_final}"
        history.append(result)
    # if no valid symbol: print advice to user
    else:
        print("Please enter a valid arithmetic operation (+, -, *, /)")
        continue

     # print result and history of past operations
    for operations in history:
        print(operations)