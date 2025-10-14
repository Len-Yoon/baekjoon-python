import sys
from queue import PriorityQueue

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
myQueue = PriorityQueue()

for i in range(n):
    num = int(input())

    if num == 0:
        if myQueue.empty():
            print("0\n")
        else:
            temp = myQueue.get()
            print(str(temp[1]) + "\n")
    else:
        myQueue.put((abs(num), num))



