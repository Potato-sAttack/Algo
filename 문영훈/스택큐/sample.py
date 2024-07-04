"""같은 숫자는 싫어(7/4)"""
def solution(arr):
    
    answer = []
    answer.append(arr[0])
    now = arr[0]
    
    for i in arr:
        if i != now:
            answer.append(i)
            now = i
        
    return answer

"""
설명 
초깃값을 배열에 넣어주고, for문돌면서 같은게 아닐때만 push

"""

"""기능 개발(7/4)"""
def solution(progresses, speeds):
    answer = []
    temp =[]
    n=0
    s=0
    for i in range(len(progresses)):
        n=100-progresses[i]
        s=speeds[i]
        if n %s ==0:
            temp.append(n//s)
        else :
            temp.append(n//s+1)
    cnt=0
    cur = temp[0]
    for i in temp:
        if i<=cur:
            cnt+=1
        else :
            answer.append(cnt)
            cnt=1
            cur=i
    answer.append(cnt)
    
    return answer
"""
설명
temp에 걸리는 기간 리스트를 만들어 주고,
앞단계의 기간이 뒷단계의 개발기간보다 길다면 앞단계와 뒷단계가 같이 나오고
뒷단계의 개발 기간이 길다면 앞단계 먼저 나와도 되는거니까 바로 append해주고 cur을 바꿔준다
마지막에 남아있는거를 마지막 줄 append를 통해서 추가해주고 리턴
"""