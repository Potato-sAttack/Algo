# sizes는 이차원베열

def solution(sizes):
    answer = 0
    
    long = []
    short = []
    
    for size in sizes:
        a,b = size
        if a > b:
            long.append(a)
            short.append(b)
        else:
            long.append(b)
            short.append(a)
            
    answer = max(long) * max(short)
    return answer

# sizes = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# print(solution(sizes))