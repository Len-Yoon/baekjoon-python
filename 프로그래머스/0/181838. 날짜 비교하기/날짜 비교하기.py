def solution(date1, date2):
    answer = 0
    
    num1 = 0
    num2 = 0
    for i in range(len(date1)):
        num1 += date1[i]
        num2 += date2[i]
        
    if date1 < date2:
        answer = 1    
    return answer