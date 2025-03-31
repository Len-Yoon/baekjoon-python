def solution(my_string, indices):
    answer = list(my_string)
    
    indices.sort()
    indices.reverse()
    
    for i in indices:
        answer.pop(i)
        
    return "".join(answer)