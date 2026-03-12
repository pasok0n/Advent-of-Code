def get_joltage(filepath: str) -> int:
    total = 0

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            battery_bank = line.strip()

            digits = [ch for ch in battery_bank if ch.isdigit()]
            if len(digits) < 12:
                raise ValueError(
                    f"Line has only {len(digits)} digits, need at least 12: "
                    f"{battery_bank!r}"
                )

            to_delete = len(digits) - 12
            stack: list[str] = []

            # left-to-right greedy
            for ch in digits:
                while to_delete > 0 and stack and stack[-1] < ch:
                    stack.pop()
                    to_delete -= 1
                stack.append(ch)

            # if deletions remain, drop from the end
            if to_delete > 0:
                stack = stack[:-to_delete]

            total += int("".join(stack[:12]))

    return total


print(get_joltage("./2025/Day_3/input"))