def solution(sizes):
    for i in sizes:
        i.sort()
    p=sizes[0][0]
    q=sizes[0][1]
    
    while sizes:
        j,s=sizes.pop()
        if p<=j:
            p=j
        if q<=s:
            q=s
    answer=p*q
    return answer
"""
정렬해서 작은 것들을 앞으로 몰고, 큰거를 뒤의 인덱스로 몬 후에
작은것들중 가장큰것 곱하기 큰것들중 가장 큰것 이 답
"""