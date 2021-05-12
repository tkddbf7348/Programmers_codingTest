def arr_sort(array, comm) :
    tmp = []
    tmp = array[comm[0]-1:comm[1]]
    tmp.sort()
    return tmp[comm[2]-1]

def solution(array, commands):
    answer = []
    
    for i in range(len(commands)) :
        answer.append(arr_sort(array, commands[i]))
    
    print(answer)
    
    
    return answer
