inputList = list()
with open('input.txt') as f:
    read_data = f.read()
    inputList = read_data.split("\n")
    inputList = [int(i) for i in inputList]

for i in inputList:
    for j in inputList:
        for k in inputList:
            if i + j + k == 2020:
                print(str(i) + ' * ' + str(j) +  ' + ' + str(k) + ' = ' + str(i*j*k))