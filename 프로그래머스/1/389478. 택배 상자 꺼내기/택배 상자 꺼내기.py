def solution(n, w, num):
    
    answer = []
    storage = []
    row = 0

    for i in range(1,n+1,w):
        list = []
        for j in range(w):
            if i+j <= n: list.append(i+j)
            else: list.append(0)
        storage.append(list)

    for i in range(len(storage)):
        if i % 2 == 1: storage[i].reverse()

    box_row = 0;
    box_col = 0;
    for i in range(len(storage)):
        if num in storage[i]:
            box_row = i
            box_col = storage[i].index(num)
            break

    for i,j in enumerate(storage):
        if i >= box_row:
            if storage[i][box_col] != 0:
                answer.append(storage[i][box_col])
                
    return len(answer)