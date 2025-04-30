##반복 가능한 객체에서 순열 구하기
from itertools import permutations

def solution(numbers):
    def sosu(num):
        if num < 2:
            return False

        for i in range(2, num//2+1):
            if num%i == 0:
                return False

        return True    
    
    temp = []
    result = []

    answer = 0

    for i in range(1, len(numbers) +1):
        temp.extend(permutations(numbers,i))
        result = [int(''.join(i)) for i in temp]

    for i in set(result):
        if sosu(i):
            answer += 1
            
    return answer