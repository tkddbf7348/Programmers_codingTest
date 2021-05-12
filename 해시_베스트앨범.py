from collections import Counter

def solution(genres, plays):
    answer = []
    
    #장르 별 가장 많이 재생된 노래 두 개씩
    #1. 노래가 많이 재생된 장르부터
    #2. 장르 내 - 많이 재생된 노래부터
    # 2-1. 고유번호(idx)가 낮은 노래부터
    #노래의 고유번호 순서대로 반환
    
    genreList = Counter(genres)
    
    playDict = {i:0 for i in genreList.keys()} #장르 구별하기
    for i in enumerate(genres) : #재생횟수 더하기
        playDict[i[1]] += plays[i[0]] #i[0] : 0, i[1] : classic
    playDict = sorted(playDict.items(), reverse=True)
    playDict.sort(key = lambda x : x[1], reverse = True)
    print("playDict : ", playDict)
    
    #리스트 묶기
    genre = [[i[0], i[1]] for i in enumerate(genres)]
    for i in range(len(plays)) :
        genre[i].append(plays[i])
    print(genre)
    
    # 높은 것 부터 뽑아냄
    for idx in range(len(playDict)) :
        tmplist = [i for i in genre if(i[1] == playDict[idx][0])]
        tmplist.sort(key = lambda x : x[2], reverse = True)
        print("tmplist : ", tmplist)
        if(len(tmplist) == 1) :
            answer.append(tmplist[0][0])
        else :
            answer.append(tmplist[0][0])
            answer.append(tmplist[1][0])
            
            
        print("answer :" , answer)
    
    
    
    return answer
