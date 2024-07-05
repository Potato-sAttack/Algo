def solution(array, commands):
    answer = []
    for i in commands:
        p = i[0] - 1
        q = i[1]
        s = i[2] - 1
        temp = array[p:q]
        temp.sort()
        k = temp[s]
        answer.append(k)
        
    return answer
