def cephalopod_math_homework(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as file:
        homework = [line.split() for line in file.read().strip().splitlines()]

    rows = len(homework)
    columns = len(homework[0])

    result: int = 0

    for column in range(columns):
        numbers = [int(homework[r][column]) for r in range(rows - 1)]
        operator = homework[rows - 1][column]

        if operator == "+":
            interim_result = sum(numbers)
        elif operator == "*":
            interim_result = 1
            for number in numbers:
                interim_result *= number

        result += interim_result

    print(result)

print(cephalopod_math_homework("./2025/Day_6/input"))