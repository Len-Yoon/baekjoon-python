def solution(myStr):
    answer = myStr.replace("a"," ").replace("b"," ").replace("c"," ")
    answer = list(map(str,answer.split()))
    if answer:
        return answer
    else:
        return ["EMPTY"]
    