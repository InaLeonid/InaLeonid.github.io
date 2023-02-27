def calculate():
    operation = input("Bitte geben Sie die gewünschte Operation ein (+, -, *, /): ")
    number1 = float(input("Bitte geben Sie die erste Zahl ein: "))
    number2 = float(input("Bitte geben Sie die zweite Zahl ein: "))

    if operation == '+':
        print(number1 + number2)
    elif operation == '-':
        print(number1 - number2)
    elif operation == '*':
        print(number1 * number2)
    elif operation == '/':
        print(number1 / number2)
    else:
        print("Ungültiger Operator! Bitte verwenden Sie einen der folgenden Operatoren: +, -, * oder /")

calculate()
