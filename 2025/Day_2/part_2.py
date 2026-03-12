def is_invalid_id(id: int) -> bool:
    id_string = str(id)
    id_length = len(id_string)
    for k in range(1, id_length // 2 + 1):
        if id_length % k != 0:
            continue
        reps = id_length // k
        if reps >= 2 and id_string == id_string[:k] * reps:
            return True
    return False

def validate_gift_shop_ids(filepath: str) -> int:
    with open(filepath, mode="r") as file:
        id_ranges = file.read().strip()
    result: int = 0
    for part in id_ranges.split(","):
        part = part.strip()
        if not part:
            continue
        start_s, end_s = part.split("-", 1)
        for id_ in range(int(start_s), int(end_s) + 1):
            if is_invalid_id(id_):
                result += id_

    return result



print(validate_gift_shop_ids("./2025/Day_2/input.txt"))