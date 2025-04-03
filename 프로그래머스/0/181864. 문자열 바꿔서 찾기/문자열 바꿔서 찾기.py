def solution(myString, pat):
    answer = 0
    
    pat = list(pat)
    for i in range(len(pat)):
        if pat[i] == 'A':
            pat[i] = 'B'
        else:
            pat[i] = 'A' 
    pat = "".join(pat)
    
    if pat in myString: answer = 1
    return answer