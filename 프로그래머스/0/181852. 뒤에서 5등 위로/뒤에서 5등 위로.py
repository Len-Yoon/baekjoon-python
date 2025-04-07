def solution(num_list):
    answer = []
    
    num_list.sort()
    for i in range(len(num_list)):
        if i >= 5:
            answer.append(num_list[i])
    return answer