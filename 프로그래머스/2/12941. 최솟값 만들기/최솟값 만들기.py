def solution(A,B):
    answer = 0
    
    A.sort(reverse= True)
    B.sort()

    for i in range(len(A)):
        answer += (A[i]*B[i])
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer