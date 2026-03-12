def scan_polymer(filepath: str) -> int:
    alphabet: list[str] = list(map(chr, range(ord('a'), ord('z')+1)))
    result: int = 10000000000
    with open(filepath, "r", encoding="utf-8") as file:
        polymer = file.read().strip()

        for reduced_polymer in [polymer.replace(ch, '').replace(ch.upper(), '') for ch in alphabet]:

            stack: list[str] = []

            for character in reduced_polymer:
                if stack and stack[-1] != character and stack[-1].lower() == character.lower():
                    stack.pop()
                else:
                    stack.append(character)
            
            result = min(result, len(stack))
    return result
    

print(scan_polymer("./2018/Day_5/input"))