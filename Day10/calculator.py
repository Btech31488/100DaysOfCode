####################### Calculator ########################3

#add

from art import logo

def add(n1, n2):
    return n1 + n2

#subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
}


def calculation():
    print(logo)
    num1 = int(input("What's the first number?: "))

    for symbol in operations:
        print(symbol)
    will_continue = True
    while will_continue:
        operation_symbol = input("Pick an operation: ")

        num2 = int(input("What's the next number?: "))


        calculation_fuction = operations[operation_symbol]
        answer = calculation_fuction(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue with {answer}, or type 'n' to start new a calculation.: ") == "y":
            num1 = answer
        else:
            will_continue = False
            calculation()


calculation()



 