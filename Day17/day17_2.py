x1, x2 = 150, 193
y1, y2 = -136, -86
ans = 0
for x in range(-1000, 1000):
    for y in range(-1000, 1000):
        xv, yv = x, y
        curX = curY = 0
        pos = False
        maxY = 0
        for times in range(500):
            curX += xv
            curY += yv
            maxY = max(maxY, curY)
            if xv > 0: xv -= 1
            if xv < 0: xv += 1
            yv -= 1
            if y1 <= curY <= y2 and x1 <= curX <= x2:
                pos = True
                break
        if pos:
            ans += 1
print(ans)