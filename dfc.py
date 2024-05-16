
#A dict containing operations
operations = {
    "add": lambda x, y: x + y,
    "subtract": lambda x, y: x - y,
    "multiply": lambda x, y: x * y,
    "divide": lambda x, y: x / y
}

x = 10
y = 5

# Iterate over each operation and print the result
for name, operation in operations.items():
    print(f"{x} {name} {y} = {operation(x, y)}")