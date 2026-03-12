def rotating_the_dial(path: str) -> int:
    password: int = 0
    dial: int = 50
    with open(path, mode="r") as file:
        for instruction in file.readlines():
            if instruction[0] == "L":
                dial = (dial - int(instruction[1:])) % 100
            else:
                dial = (dial + int(instruction[1:])) % 100

            if dial == 0:
                password += 1

    return password


print(rotating_the_dial("./2025/Day_1/input.txt"))