import itertools

def solution(word):
    arr = ['A','E','I','O','U']
    dict = []
    for i in range(5):
        for v in itertools.product(arr, repeat= i+1):
            dict.append("".join(v))

        dict.sort()
    return dict.index(word)+1