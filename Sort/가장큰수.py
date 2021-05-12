def solution(numbers):
    numList = list(map(str, numbers))
    numList.sort(key = lambda x:x*3, reverse = True)
    #print(numList)
    #print("".join(numList))
    
    return str(int("".join(numList)))
