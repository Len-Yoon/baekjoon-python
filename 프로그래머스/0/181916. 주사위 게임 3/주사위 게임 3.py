def solution(a, b, c, d):
    answer = 0
    arr = [a,b,c,d]
    a1 = []
    a2 = []
    
    arr.sort()
    array = set(arr)
    ar = list(array)
    
    if len(ar) == 1:
        answer = 1111*a
        
    elif len(ar) == 2:
        if arr[1] != arr[2]:
            answer = (arr[1]+arr[2]) * abs(arr[1]-arr[2])
        elif arr[1] == arr[2]:
            if arr[2] == arr[3] and arr[0] != arr[1]:
                answer = ((10*arr[3]+arr[0])**2)
            else:
                answer = ((10*arr[0]+arr[3])**2)
                
    elif len(ar) == 4:
        answer = arr[0]
        
    elif len(ar) == 3:
        for i in arr:
            if i not in a1:
                a1.append(i)
            else:
                if i not in a2:
                    a2.append(i)
        a1.remove(a2[0])           
            
        answer = a1[0] * a1[1]    
                

    return answer
