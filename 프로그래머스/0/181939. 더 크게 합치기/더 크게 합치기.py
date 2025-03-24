def solution(a, b):
    answer = 0
    
    c = str(a) + str(b)
    d = str(b) + str(a)
    
    if int(c) > int(d):
        answer = int(c)
    else:
        answer = int(d)
    
    return answer