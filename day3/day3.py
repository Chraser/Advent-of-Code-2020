with open("input.txt", "r") as f:
    content = f.read().strip().split('\n')
    offsets = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    
    total = 1
    for x_offset, y_offset in offsets:
        pos_x = 0
        pos_y = 0
        count = 0
        while pos_y < len(content):
            if content[pos_y][pos_x] == '#':
                count = count + 1
            
            pos_x = (pos_x + x_offset) % len(content[0])
            pos_y = pos_y + y_offset
        total = total * count

    print("The number of trees encountered is " + str(total))