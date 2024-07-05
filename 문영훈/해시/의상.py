"""의상 문제(7/4)"""

def solution(clothes):
    
    c_dic={}
    for _,j in clothes:
        if j in c_dic:
            c_dic[j]+=1
        else:
            c_dic[j]=1
    
    answer =1
    for k in c_dic:
        answer *= (c_dic[k]+1) 
    
    return answer-1

"""
조합 문제 - A - m개, B - n개 , C-z개 있다고 가정
            다 하나씩 입는다 가정 - M*N*Z
            두 종류 중 하나씩 입는다 가정 - mn+nz+mz
            하나씩만 입는다 가정 - m+n+z
            아예 안 입는 경우의 수 1
            (m+1)(n+1)(z+1)=(mn+m+n+1)(z+1)=mnz+mz+nz+mn+m+n+z+1
            여기서 1을 빼주면 아예안 입는 경우의 수 빠지므로.. 종류를 key로하고 그 종류에 해당하는 수를 value로하는 
            해시를 만들어 각 value에 +1을 한 후에 곱하기해서 계산후 마지막 아예안 입는 경우의수 빼주고 리턴

"""

