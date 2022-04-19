import random

inputN = random.randrange(1, 1000)
inputN = 1000
#inputArr = [[0]*4 for _ in range(inputN)]
#inputArr= [[0]*inputN]*inputN
inputArr = []
for i in range(0, inputN):
    inputArr.append([])
    for j in range(0, inputN):
        inputArr[i].append(0)


for i in range(0, inputN):
    for j in range(i, inputN):
        if i != j:
            cc = random.randrange(0, 11)
            inputArr[i][j] = cc
            inputArr[j][i] = cc

#
# print(inputN)
# for i in range(0, inputN):
#     for j in range(0, inputN):
#         print(inputArr[i][j], end=" ")
#     print("")


f = open("./output.txt", 'w')
f.write(str(inputN))
f.write("\n")
for i in range(0, inputN):
    for j in range(0, inputN):
        data = str(inputArr[i][j]) + " "
        f.write(data)
    f.write("\n")

f.close()