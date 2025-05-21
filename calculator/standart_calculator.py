from art import logo


def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}


def calculator():
    """
    The function does the standard math calculations for the specified numbers and operators.
    :return: Calculate the result and repeats the process.
    """

    print(logo)
    should_accumulate = True
    num1 = float(input("What's the first number?: "))

    while should_accumulate:
        for the_op in operations:
            print(the_op)

        op = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        result = operations[op](num1, num2)
        print(f"{num1} {op} {num2} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()
