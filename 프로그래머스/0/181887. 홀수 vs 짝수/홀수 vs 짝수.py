def solution(num_list):
    odd = 0
    even = 0
    
    for i in range(len(num_list)):
        if i % 2 == 0:
            even += num_list[i]
        else:
            odd += num_list[i]
            
    if odd > even:
        return odd
    else:
        return even