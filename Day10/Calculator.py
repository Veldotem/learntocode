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
def calculator():
    num1 = float(input("Enter the first number:\n"))
    for symbol in operations:
        print(symbol)

    should_continue = True
    snew = True
    while should_continue:
        operation_symbol = input("Pick an operation from the menu:\n")
        num2 = float(input("Enter the second number:\n"))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} + {num2} = {answer}")
        num1 = answer
        scontinue = input("would you like to continue calculating with the previous answer?y/n\n")
        if scontinue == "n":
            snew = input("Do you want to start a new calculation?y/n\n")
            if snew == "y":
                calculator()
            else:
                should_continue = False
                exit("Thanks for using this calculator!")

calculator()