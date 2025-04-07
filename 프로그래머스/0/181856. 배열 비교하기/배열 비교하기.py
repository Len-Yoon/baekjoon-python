def solution(arr1, arr2):
    answer = 0
    if len(arr1) < len(arr2):
        answer = -1;
    elif len(arr1) > len(arr2):
        answer = 1
    else:
        arr1_num = 0
        arr2_num = 0
        for i in range(len(arr1)):
            arr1_num += arr1[i]
            arr2_num += arr2[i]
        
        if arr1_num < arr2_num:
            answer = -1
        elif arr1_num > arr2_num:
            answer = 1
        else:
            answer = 0
            
    return answer