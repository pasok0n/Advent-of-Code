def tachyon_manifold(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as file:
        manifold = [list(line) for line in file.read().strip().splitlines()]

    width = len(manifold[0])
    height = len(manifold)
    split_count: int = 0

    start_position = manifold[0].index("S")  
    manifold[1][start_position] = 1
    current_height = 2
    current_position = start_position
    while current_height < height:
        while current_position < width:
            if isinstance(manifold[current_height-1][current_position],int) and manifold[current_height][current_position] == "^":
                split_count += 1
                if isinstance(manifold[current_height][current_position-1],int):
                    temp_number = manifold[current_height][current_position-1]
                    manifold[current_height][current_position-1] = temp_number + int(manifold[current_height-1][current_position])
                elif manifold[current_height][current_position-1] == ".":
                    manifold[current_height][current_position-1] = int(manifold[current_height-1][current_position])
                
                if isinstance(manifold[current_height][current_position+1],int):
                    temp_number = int(manifold[current_height][current_position+1])
                    manifold[current_height][current_position+1] = temp_number + int(manifold[current_height-1][current_position])
                elif manifold[current_height][current_position+1] == ".":
                    manifold[current_height][current_position+1] = int(manifold[current_height-1][current_position])
                
            elif isinstance(manifold[current_height-1][current_position],int) and manifold[current_height][current_position] == ".":
                manifold[current_height][current_position] = int(manifold[current_height-1][current_position])
            elif isinstance(manifold[current_height-1][current_position],int) and isinstance(manifold[current_height][current_position],int):
                temp_number = manifold[current_height][current_position]
                manifold[current_height][current_position] = temp_number + int(manifold[current_height-1][current_position])
            current_position += 1
        
        current_position = 0
        current_height += 1
    result = 0
    for x in manifold[height-1]:
        if isinstance(x,int):
            result += x
    return result



print(tachyon_manifold("./2025/Day_7/input"))