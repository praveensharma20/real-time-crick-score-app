from tabulate import tabulate

data = [
    ["Alice", 24, "Engineer"],
    ["Bob", 30, "Designer"],
    ["Charlie", 28, "Teacher"]
]

headers = ["Name", "Age", "Occupation"]

print(tabulate(data, headers=headers, tablefmt="grid"))