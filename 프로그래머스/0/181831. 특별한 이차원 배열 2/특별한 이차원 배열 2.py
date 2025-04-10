def solution(arr):
    
    answer = []
    num = 1
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == arr[j][i]:
                answer.append(1)
            else:
                answer.append(0)
    if 0 in answer:
        num = 0
    
    return num