def get_joltage(filepath: str) -> int:
    with open(filepath, mode="r") as file:
        battery_banks = [bank.rstrip("\n") for bank in file]
    
    result: int = 0
    for battery_bank in battery_banks:
        best_right = -1
        best = -1
        for character in reversed(battery_bank):
            digit = ord(character) - ord("0")
            if 0 <= digit <= 9:
                if best_right != -1:
                    best = max(best, digit*10 + best_right)
                best_right = max(best_right, digit)
        result += best

    return result

print(get_joltage("./2025/Day_3/input"))