def solution(numbers):
    answer = ''
    numbers = list(map(str,numbers))
    #x*3을 하게 되면 [3, 310, 30] -> [333, 310310310, 303030] 이렇게 된다. 자릿수를 맞춰 비교하기 위함
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int(''.join(numbers)))