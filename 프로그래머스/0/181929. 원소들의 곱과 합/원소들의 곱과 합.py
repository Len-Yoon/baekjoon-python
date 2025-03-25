def solution(num_list):
    answer = 0
    a = 0
    b = 1
    for i in range(len(num_list)):
        a = a + num_list[i]
        b = b * num_list[i]
        
    if (a**2) > b:
        answer = 1
    else:
        answer = 0
    return answer