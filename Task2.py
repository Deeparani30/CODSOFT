def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return 'Please enter valid numbers.'

    if operation == 'add':
        return f'Result: {num1 + num2}'
    elif operation == 'subtract':
        return f'Result: {num1 - num2}'
    elif operation == 'multiply':
        return f'Result: {num1 * num2}'
    elif operation == 'divide':
        if num2 == 0:
            return 'Error: Division by zero'
        else:
            return f'Result: {num1 / num2}'
    else:
        return 'Invalid operation.'


def main():
    print("Simple Calculator")

    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    print("Choose operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter the operation number (1-4): ")

    operations = {
        '1': 'add',
        '2': 'subtract',
        '3': 'multiply',
        '4': 'divide'
    }

    operation = operations.get(choice)

    if operation:
        result = calculate(num1, num2, operation)
        print(result)
    else:
        print('Invalid operation number. Please enter a number between 1 and 4.')


if __name__ == "__main__":
    main()
