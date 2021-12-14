import numpy as np
data = [line.strip() for line in open("input.txt", 'r')]
new_data = []
for s in data:
    line = []
    for j in s:
        line.append(int(j))
    new_data.append(line)
data = new_data
new_data = np.transpose(new_data)
clone_data = data
# print((len(new_data)))
while (len(clone_data) > 1):
    for i in range(len(new_data)):
        count0 = 0
        for j in new_data[i]:
            if j == 0:
                count0 += 1
            else:
                count0 -= 1
        # print(count0)
        if count0 > 0:
            # gamma_rate += "0" #prob 1
            filter_data = [x for x in clone_data if x[i] == 0]
        elif count0 <= 0:
            # gamma_rate += "1" #prob 1
            filter_data = [x for x in clone_data if x[i] == 1]
        clone_data = filter_data
        # print(clone_data)
        new_data = np.transpose(clone_data)
        # print(len(clone_data))
        if (len(clone_data) == 1):
            break
oxygen = ""
for i in clone_data[0]:
    oxygen += str(i)
# print(oxygen)
# print(data)
new_data = np.transpose(data)
clone_data = data
# print(new_data)
while (len(clone_data) > 1):
    for i in range(len(new_data)):
        count0 = 0
        for j in new_data[i]:
            if j == 0:
                count0 += 1
            else:
                count0 -= 1
        # print(count0)
        if count0 > 0:
            # gamma_rate += "0" #prob 1
            filter_data = [x for x in clone_data if x[i] == 1]
        elif count0 <= 0:
            # gamma_rate += "1" #prob 1
            filter_data = [x for x in clone_data if x[i] == 0]
        clone_data = filter_data
        # print(clone_data)
        new_data = np.transpose(clone_data)
        if (len(clone_data) == 1):
            break
co2 = ""
for i in clone_data[0]:
    co2 += str(i)
print(int(oxygen,2)*int(co2,2))