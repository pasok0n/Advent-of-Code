def rotating_the_dial(path: str) -> int:
    password: int = 0
    dial: int = 50
    with open(path, mode="r") as file:
        for instruction in file.readlines():
            rotation = int(instruction[1:]) # using good ol' brute force
            for i in range(0, rotation):    # hearing each click of the dial
                if instruction[0] == "L":
                    absolute = dial - 1
                    dial = (absolute) % 100
                else:
                    absolute = dial + 1
                    dial = (absolute) % 100
                if dial == 0:
                    password += 1

    return password


print(rotating_the_dial("./2025/Day_1/input.txt"))