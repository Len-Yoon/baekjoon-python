def solution(picture, k):
    new_pic = ""
    new_picture = []

    for i in picture:
        new_pic = ""
        for j in i:
            new_pic += j*k
        for j in range(k):
            new_picture.append(new_pic)
        
    return new_picture