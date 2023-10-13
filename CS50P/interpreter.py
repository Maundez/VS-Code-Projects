def main():
    expression = input("Expression: ")
    x_factor, y_factor, operator = get_factors(expression)
    my_interpreter(x_factor, y_factor, operator)

def get_factors(expression):
    expression = expression.split(" ")
    x_factor = expression[0]
    y_factor = expression[2]
    operator = expression[1]
    print(f"x is {x_factor}, y is {y_factor}, The operator is {operator}")
    return x_factor, y_factor, operator

def my_interpreter(x_factor, y_factor, operator):
    print(f"{x_factor} {operator} {y_factor}")

main()