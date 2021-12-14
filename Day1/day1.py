data = [line.strip() for line in open("input.txt", 'r')]
data = [int(i) for i in data]
# print(data)
count = 0
for i in range(len(data) - 1):
    if data[i] < data[i+1]:
        count += 1
print(count)

count = 0
for i in range(len(data) - 3):
    if (data[i] + data[i+1] + data[i+2] < data[i+1] + data[i+2] + data[i+3]):
        count += 1
print(count)
