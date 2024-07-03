def solution(arr):
    answer = []
    answer.append(arr[0])
    cur = arr[0]
    
    for i in arr:
        if i != cur:
            answer.append(i)
            cur = i
    
    return answer

arr = list(map(int, input().split(',')))
print(arr)
