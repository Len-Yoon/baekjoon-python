def solution(order):
    answer = 0
    
    for i in order:
        if i in ["iceamericano", "americanoice","hotamericano", "americanohot","americano","anything"]:
            answer += 4500
        else:
            answer += 5000
            
    return answer