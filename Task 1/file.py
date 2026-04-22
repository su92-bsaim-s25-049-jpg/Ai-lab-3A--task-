import re

def calculator():
    print("Enter full expression (type 'exit' to quit)")

    while True:
        expr = input("Enter expression: ")

        if expr.lower() == "exit":
            break

        expr = expr.replace("×", "*").replace("÷", "/")
        expr = re.sub(r'(\d)\(', r'\1*(', expr)

        try:
            result = eval(expr)
            print("Result:", result)
        except Exception as e:
            print("Invalid expression:", e)

calculator()