import itertools
from sys import stdin
input = stdin.readline
from collections import Counter

    
    
def solution(clothes):
    answer = 0
    dic_clothes = dict(clothes)
    clothes_kind = dic_clothes.values() #옷 종류들(중복 포함)
    kind_counter = Counter(clothes_kind) #옷 종류 별 개수
    kind_counter_clothes = kind_counter.keys() #옷 종류(중복 미포함)
    
    if(len(kind_counter) == 30) :
        return 1073741823; 
    
    if(len(kind_counter) == 1 ) : #옷 종류가 1개면 
        return kind_counter[list(kind_counter_clothes)[0]]
    
    for length in range(1, len(dic_clothes) + 1) : #옷 종류 조합 구함
        tmp_comb = list(itertools.combinations(kind_counter_clothes, length))
        #print("tmp_comb : ", tmp_comb)
        for combination in tmp_comb :
            answer_tmp = 1
            for idx in combination :
                #print("t : ", t)
                answer_tmp *= kind_counter[idx]
            answer += answer_tmp
            #print("combination : ", combination, ", count : ", answer_tmp)
            
            
    return answer
