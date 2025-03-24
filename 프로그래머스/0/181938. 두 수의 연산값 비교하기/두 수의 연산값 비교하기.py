def solution(a, b):
    answer = 0
    c = int(str(a) + str(b))
    
    if c >= (2*a*b):
        answer = c
    else:
        answer = 2*a*b
    return answer