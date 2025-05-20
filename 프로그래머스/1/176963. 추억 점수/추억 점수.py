def solution(name, yearning, photo):
    answer = []
    
    photo_dic = dict(zip(name, yearning))
    
    for i in photo:
        score = 0
        for j in i:
            score += int(photo_dic.get(j,0))
        answer.append(score)
    return answer