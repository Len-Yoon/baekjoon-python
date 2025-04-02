def solution(arr):
    count = 0
    
    while(True):
        next = []  
        for i in arr:
            if i >= 50 and i % 2 == 0 :
                next.append(int(i/2))
            elif i < 50 and i % 2 == 1:
                next.append(i*2 + 1)
            else:
                next.append(i)
        
        if arr == next:
            break
        else:
            count = count + 1
            arr = next
        
    return count