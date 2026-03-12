def ingredient_checker(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        ingredient_id_ranges, _ = f.read().split("\n\n", 1)

    id_ranges = sorted((tuple(map(int, line.split("-"))) for line in ingredient_id_ranges.splitlines()), key=lambda x: x[0])

    merged = []
    for start, end in id_ranges:
        if not merged or start > merged[-1][1] + 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    return sum(end - start + 1 for start, end in merged)

print(ingredient_checker("./2025/Day_5/input"))