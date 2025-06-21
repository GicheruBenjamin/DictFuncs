from typing import Callable

Operation = Callable[[int, int], float]

def add(a: int, b: int) -> float:
    return a + b

def sub(a: int, b: int) -> float:
    return a - b

def mul(a: int, b: int) -> float:
    return a * b

def div(a: int, b: int) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return 0.0

ops: dict[str, Operation] = {
    "add": add,
    "sub": sub,
    "mul": mul,
    "div": div
}

def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def main():
    value_one = get_int("Enter first number: ")
    value_two = get_int("Enter second number: ")
    operation = input("Enter operation (add, sub, mul, div): ").strip()

    if operation in ops:
        result = ops[operation](value_one, value_two)
        print(f"Result: {result}")
    else:
        print(f"Invalid operation: {operation}")

if __name__ == "__main__":
    main()
