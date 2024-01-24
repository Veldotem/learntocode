def add(n1, n2):
    """Add two numbers"""
    return n1 + n2
def subtract(n1, n2):
    """Subtract two numbers"""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def divide(n1, n2):
    """Divide two numbers"""
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))

for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from the menu:\n")

answer = operations[operation_symbol](num1, num2)

print(f"{num1} + {num2} = {answer}")