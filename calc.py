op = input("Enter the operator: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if op == "+":
    result = num1 + num2
    print(round(result,3))
elif op == "-":
    result = num1 - num2
    print(round(result,3))
elif op == "*":
    result = num1 * num2
    print(round(result,3))
elif op == "/":
    result = num1 / num2
    print(round(result,3))
elif op == "^" or op == "**":
    result = num1 ** num2
    print(round(result,3))
elif op == "%":
    result = num1 % num2
    print(round(result,3))
else:
    print("Operation not supported")
