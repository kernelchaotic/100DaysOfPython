
print("""
 _____________________
|  _________________  |
| | TI 6 9 4 2 0    | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")

def calculator():

    # addition
    def add(n1, n2):
        return n1 + n2

    # subtraction
    def subtract(n1, n2):
        return n1 - n2

    # multiplication
    def multiply(n1, n2):
        return n1 * n2

    # division
    def divide(n1, n2):
        if (n1 / n2) % 1 == 0:
            return int(n1 / n2)
        else:
            return n1 / n2

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    user_finished = False
    num1 = float(input("What is the first number?:  "))

    while not user_finished:
        for symbol in operations:
            print(symbol)
        selected_operator = input("Pick an operation:  ")
        num2 = float(input("What is the next number?:  "))
        calculation_operator = operations[selected_operator]
        answer = calculation_operator(num1, num2)

        print(f"{num1} {selected_operator} {num2} = {answer}\n")

        continue_calculating = input(f"Would you like to continue calculating with {answer}? Y/N:  ").lower()
        if continue_calculating == "y" or continue_calculating == "yes":
            num1 = answer
        elif continue_calculating == "n" or continue_calculating == "no":
            another_calculation = input("\nWould you like to do another calculation? Y/N:  ").lower()
            if another_calculation == "y" or another_calculation == "yes":
                calculator()
            else:
                user_finished = True
        else:
            print("I'm sorry. I did not understand that.")


calculator()

print("Have a great day!")
