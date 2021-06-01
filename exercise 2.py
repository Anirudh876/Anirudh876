print("Welcome to pycharm calculator")
print("Choose the operator \n + for addition \n - for substraction \n * for multiplication \n / for Division")
operator = input()
List_of_operators = ["+", "-", "*", "/"]
if operator not in List_of_operators:
    print("Error")
else:
    print("Enter two numbers")
    number1 = int(input())
    number2 = int(input())
if operator == "+":
    if number1 == 56 and number2 == 9:
        print("77")
    elif number1 == 9 and number2 == 56:
        print("77")
    else:
        print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    if number1 == 45 and number2 == 3:
        print("555")
    elif number1 == 3 and number2 == 45:
        print("555")
    else:
        print(number1 * number2)
elif operator == "/":
    if number1 == 56 and number2 == 6:
        print("47")
    else:
        print(number1 / number2)

# calculator.save("my library.html")