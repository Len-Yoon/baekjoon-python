def solution(myString):
    answer = ''
    
    for i in range(len(myString)):
        if myString[i] == 'A' or myString[i] == 'a':
            answer += myString[i].upper()
        else:
            answer += myString[i].lower()
    return answer