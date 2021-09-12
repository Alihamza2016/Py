number1 = int(input("Enter a number(s): "))
operator = input("Enter an operator: ")
number2 = int(input("Enter another number(s): "))
answer = 0
if operator == "+" :
    answer = number1 + number2
elif operator == "-":
    answer = number1 - number2
elif operator == "/" and answer != 0:
    answer = number1 / number2
elif operator == "*":
    answer = number1 * number2
print (answer)