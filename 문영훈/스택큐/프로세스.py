def solution(priorities, location):
    answer=0
    data=[]
    cnt=0
    for i in enumerate(priorities):
        data.append(i)    
    
    while data :
        l,v=data.pop(0)
        checkvalue=1
        for _,k in data:
            if v>=k:
                continue
            else :
                checkvalue=0
                break
        
        if checkvalue == 0:
            data.append((l, v))
        else:
            answer += 1
            if l == location:
                break
                
    return answer


"""
인덱스를 같이 입력해서 튜플을 원소로가지는 리스트 만들기
그 리스트를 돌면서 팝을해서 데이터를 받아와 다시 우선순위를 비교해서 가져온 숫자가 우선순위가 가장크다면 checkvalue가
1을유지
만약 checkvalue가 1이라면
pop한상태로 큐를 빠져나가, answer에 빠져나간 순위가 +1되고 만약 그 value의 인덱스가 내가찾던 location과 같다면,
반복문을 멈추고 answer에 기록된 우선순위를 반환
"""