def solution(n, k):
    answer = []
    
    for i in range(0,n+1,k):
        if i != 0:
            answer.append(i)
    return answer