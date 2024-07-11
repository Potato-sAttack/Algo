from itertools import permutations
def solution(numbers):
    answer = []
    numbers = list(map(str, numbers))
    list1 = list()
    
    for i in range(1,len(numbers)+1):
        for j in permutations(numbers, i):
            a = int(''.join(j))
            list1.append(a)
                
    for i in list1:
        cnt = 0
        if i <2: 
            continue
        for x in range(2, int(i**0.5)+1):
            if i % x == 0:  
                cnt = 1
                break
        if cnt == 0 :
            answer.append(i)
            
    return len(set(answer))