inputList = list()
with open('input.txt') as f:
    read_data = f.read()
    inputList = read_data.split("\n")

valid = 0
for item in inputList:
    parts = item.split(" ")
    ranges = parts[0].split("-")
    lower = int(ranges[0]) - 1
    upper = int(ranges[1]) - 1
    character = parts[1][0]
    string = parts[2]
    if string[lower] == character and string[upper] != character:
        valid = valid + 1
    elif string[lower] != character and string[upper] == character:
        valid = valid + 1


    '''
    count = 0
    for char in string:
        if char == character:
            count = count + 1
    if count >= lower and count <= upper:
        valid = valid + 1
    '''
print(valid)