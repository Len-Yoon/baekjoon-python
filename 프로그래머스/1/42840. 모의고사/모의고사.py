def solution(answers):
    answer = []
    
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    c1,c2,c3 = 0,0,0
    
    for i in range(len(answers)):
        num1, num2, num3 = i%5, i%8, i%10

        if answers[i] == student1[num1]:
            c1 += 1
        if answers[i] == student2[num2]:
            c2 += 1
        if answers[i] == student3[num3]:
            c3 += 1
    
    maxNum = max(c1,c2,c3)
    
    if maxNum == c1:
        answer.append(1)
    if maxNum == c2:
        answer.append(2)
    if maxNum == c3:
        answer.append(3)
    return answer