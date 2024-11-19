

# # for x in range(1,5):
# #     for y in range(1,11):
# #         print(x,"x",y,"=",(x*y))


# for hour in range(1, 13):
#     for minute in range(0, 60): 
#         for second in range(0, 60): 
#             print(f"{hour:0}:{minute:0}:{second:0}") 

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("Choose an operation: +, -, *, /")
operation = input("Enter the operation you want to perform: ")

try:

    if operation == '+':
        output = num1 + num2
        print(f"{num1} + {num2} = {output}")
    elif operation == '-':
        output = num1 - num2
        print(f"{num1} - {num2} = {output}")
    elif operation == '*':
        output = num1 * num2
        print(f"{num1} * {num2} = {output}")
    elif operation == '/':
        # Check for division by zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            output = num1 / num2
            print(f"{num1} / {num2} = {output}")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")
except ValueError:
    print("Please enter valid numbers")
