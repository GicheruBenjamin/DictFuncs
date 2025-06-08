
from typing import Callable

def add(a : int, b : int) -> int:
    try:
        return a + b
    except Exception as e:
        print(f"Error addind stuff coz of {e}")
        return 0


def sub(a : int, b : int) -> int:
    try:
        return a - b
    except Exception as e:
        print(f"Error subtracting stuff coz of {e}")
        return 0

def mul(a : int, b : int) -> int:
    try:
        return a * b
    except Exception as e:
        print(f"Error multiplying stuff coz of {e}")
        return 0


def div(a : int, b : int) -> int:
    try:
        return a / b
    except Exception as e:
        print(f"Error dividing stuff coz of {e}")
        return 0

ops : dict[str, Callable] = {
    "add" : add,
    "sub" : sub,
    "mul" : mul,
    "div" : div
}

def main():
    value_one: int = int(input("Enter first number: "))
    value_two: int = int(input("Enter second number: "))
    operation: str = input("Enter operation: ")
    if operation in ops:
        result: int = ops[operation](value_one, value_two)
        print(f"Result: {result}")
    else:
        print(f"Invalid operation: {operation}")

if __name__ == "__main__":
    main()
