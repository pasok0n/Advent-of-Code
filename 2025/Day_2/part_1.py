def validate_gift_shop_ids(filepath: str) -> int:
    with open(filepath, mode="r") as file:
        id_ranges = file.read().strip()
    result: int = 0
    for part in id_ranges.split(","):
        part = part.strip()
        if not part:
            continue
        start_s, end_s = part.split("-", 1)
        for id in range(int(start_s), (int(end_s)+1)):
            id_string = str(id)
            if (len(id_string)%2)==0:
                middle = len(id_string) // 2
                if int(id_string[:middle]) == int(id_string[middle:]):
                    print(id)
                    result += id

    return result



print(validate_gift_shop_ids("./2025/Day_2/input.txt"))