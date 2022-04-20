import random

inputN = random.randrange(10, 11)
inputArr = []
for i in range(0, inputN):
    inputArr.append([])
    for j in range(0, inputN):
        inputArr[i].append(0)


for i in range(0, inputN):
    for j in range(i, inputN):
        if i != j:
            cc = random.randrange(2, 11)
            if cc % 2 != 0:
                cc = cc -1
            inputArr[i][j] = cc
            inputArr[j][i] = cc

f = open("./output.txt", 'w')
f.write(str(inputN))
f.write("\n")
for i in range(0, inputN):
    for j in range(0, inputN):
        data = str(inputArr[i][j]) + " "
        f.write(data)
    f.write("\n")
f.close()