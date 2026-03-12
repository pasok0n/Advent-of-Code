def ingredient_checker(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        ingredient_db_1, ingredient_db_2 = f.read().split("\n\n", 1)

    ingredient_id_ranges = [tuple(map(int, line.split("-"))) for line in ingredient_db_1.splitlines()]
    ingredient_ids = [int(line) for line in ingredient_db_2.splitlines()]
    fresh_ingredients: int = 0
    for id_ in ingredient_ids:
        if any(start <= id_ <= end for start, end in ingredient_id_ranges):
            fresh_ingredients += 1

    return fresh_ingredients

print(ingredient_checker("./2025/Day_5/input"))