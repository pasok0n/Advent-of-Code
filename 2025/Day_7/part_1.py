def tachyon_manifold(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as file:
        manifold = [list(line) for line in file.read().strip().splitlines()]

    width = len(manifold[0])
    height = len(manifold)
    split_count: int = 0

    start_position = manifold[0].index("S")  
    manifold[1][start_position] = "|"
    current_height = 2
    current_position = start_position
    while current_height < height:
        while current_position < width:
            if manifold[current_height-1][current_position] == "|" and manifold[current_height][current_position] == "^":
                split_count += 1
                manifold[current_height][current_position-1] = "|"
                manifold[current_height][current_position+1] = "|"
            elif manifold[current_height-1][current_position] == "|" and manifold[current_height][current_position] == ".":
                manifold[current_height][current_position] = "|"
            current_position += 1
        
        current_position = 0
        current_height += 1
    
    return split_count



print(tachyon_manifold("./2025/Day_7/input"))