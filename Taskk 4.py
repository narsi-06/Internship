def calculator():
    print("Basic Calculator")
    
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed"
    elif operator == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            return "Error: Modulo by zero is not allowed"
    else:
        return "Invalid operator"

    return f"Result: {result}"

print(calculator())
