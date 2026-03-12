def scan_polymer(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as file:
        polymer = file.read().strip()

        stack: list[str] = []

        for character in polymer:
            if stack and stack[-1] != character and stack[-1].lower() == character.lower():
                stack.pop()
            else:
                stack.append(character)
        print("".join(stack))
        return len(stack)
    

print(scan_polymer("./2018/Day_5/input.txt"))