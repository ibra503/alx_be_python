def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Input error: Unsupported operation."


num1 = float(input("Enter number1 "))
num2 = float(input("Enter number2 "))
operation = input("Enter the operation (add, subtract, multiply, divide): ")

result = perform_operation(num1, num2, operation)
print (f"result: {result}")









