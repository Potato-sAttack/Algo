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