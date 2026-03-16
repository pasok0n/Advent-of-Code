def cephalopod_math_homework(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as file:
        homework = file.read().splitlines()

    rows = len(homework)
    columns = len(homework[0])

    result: int = 0

    column = columns-1
    while column >= 0:
        while column >= 0 and all(homework[row][column] == " " for row in range(rows)):
            column -= 1

        right = column
        while column >= 0 and not all(homework[row][column] == " " for row in range(rows)):
            column -= 1
        left = column + 1

        operator = homework[rows-1][left]

        numbers = []

        for block_column in range(right, left - 1, -1):
            digits = []
            for row in range(rows - 1):
                character = homework[row][block_column]
                if character.isdigit():
                    digits.append(character)
            if digits:
                numbers.append(int("".join(digits)))

        if operator == "+":
            result += sum(numbers)
        elif operator == "*":
            interim_result: int = 1
            for number in numbers:
                interim_result *= number
            result += interim_result

    return result
            

print(cephalopod_math_homework("./2025/Day_6/input"))