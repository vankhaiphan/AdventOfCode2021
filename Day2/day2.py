data = [line.strip() for line in open("input.txt", 'r')]
data = [line.split() for line in data]
horizontal = 0
depth = 0
aim = 0
print(data)
for i in data:
    if i[0] == 'forward':
        horizontal += int(i[1]) #prob 1 & 2
        depth += aim*int(i[1]) #prob 2
    elif i[0] == 'up':
        # depth -= int(i[1]) #prob 1
        aim -= int(i[1]) #prob 2
    elif i[0] == 'down':
        # depth += int(i[1]) #prob 1
        aim += int(i[1]) #prob 2

print(horizontal)
print(depth)
print(horizontal*depth)