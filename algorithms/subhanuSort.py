import time
from colors import *


def subhanu_sort(data, drawData, timeTick):
    size = len(data)
    c = 0
    for i in range(size - 1):
        if data[i] > data[i + 1] and c <= (size - 3) * size:
            data[i], data[i + 1] = data[i + 1], data[i]
            c += 1
            i = -1
            drawData(data, [YELLOW if x == i or x == i + 1 else BLUE for x in range(len(data))])
            time.sleep(timeTick)

    drawData(data, [BLUE for x in range(len(data))])
