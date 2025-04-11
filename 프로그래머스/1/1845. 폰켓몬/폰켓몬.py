import collections
def solution(nums):
    myNum = len(nums)//2

    countDict = dict(collections.Counter(nums))

    if (len(countDict) >= myNum):
        return myNum
    else : 
        return len(countDict)
    