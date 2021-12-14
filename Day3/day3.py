import numpy as np
data = [line.strip() for line in open("in.txt", 'r')]
# data = [line.split() for line in data]
new_data = []
for s in data:
    line = []
    for j in s:
        line.append(int(j))
    new_data.append(line)
data = new_data
# print(data)
new_data = np.transpose(new_data)
# print(new_data)
clone_data = data
gamma_rate = ""
for i in range(len(new_data)):
    count0 = 0
    for j in new_data[i]:
        if j == 0:
            count0 += 1
        else:
            count0 -= 1
    print(count0)
    if count0 > 0:
        gamma_rate += "0" #prob 1
        # filter_data = [x for x in clone_data if x[i] == 0]
    elif count0 <= 0:
        gamma_rate += "1" #prob 1
        # filter_data = [x for x in clone_data if x[i] == 1]
    # clone_data = filter_data
    # print(clone_data)
# print(clone_data)
# prob 1
epsilon_rate = ""
for i in gamma_rate:
    if i == "1":
        epsilon_rate += "0"
    else:
        epsilon_rate += "1"
print(gamma_rate," ", epsilon_rate)
print(int(gamma_rate,2)*int(epsilon_rate,2))
