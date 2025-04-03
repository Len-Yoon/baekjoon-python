def solution(myString, pat):
    
    num = myString.rfind(pat)
    return myString[:num+len(pat)]