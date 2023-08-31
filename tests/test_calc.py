
def test_add():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(1, 3) == -2

def test_mul():
    assert mul(2, 3) == 6
    assert mul(0, 5) == 0
    assert mul(-2, 4) == -8

def test_divide():
    assert divide(6, 3) == 2
    assert divide(0, 5) == 0
    assert divide(10, 2) == 5
    assert divide(8, 0) is None  # Division by zero

# Main calculator functions
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2 if num2 != 0 else None

# Main calculator logic
def main():
    try:
        num_a = float(input("Enter number: "))
        op = input('Enter "+", "-", "*", "/" ')
        num_b = float(input("Enter number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    else:
        if op in ['+', '-', '*', '/']:
            if op == '+':
                print(f"{num_a} {op} {num_b} = {add(num_a, num_b)}")
            elif op == '-':
                print(f"{num_a} {op} {num_b} = {sub(num_a, num_b)}")
            elif op == '*':
                print(f"{num_a} {op} {num_b} = {mul(num_a, num_b)}")
            else:
                result = divide(num_a, num_b)
                if result is not None:
                    print(f"{num_a} {op} {num_b} = {result}")
                else:
                    print("Cannot divide by zero")
        else:
            print("Enter correct operator")

if __name__ == "__main__":
    main()