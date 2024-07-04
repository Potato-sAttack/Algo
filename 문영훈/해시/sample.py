"폰켄몬 문제"

def solution(nums):
    max_choice_num=len(nums)/2
    a_dic={}
    for num in nums:
        if num in a_dic:
            a_dic[num]+=1
        else:
            a_dic[num]=1
    
    if len(a_dic)>=max_choice_num:
        answer=max_choice_num
    else:
        answer=len(a_dic)  
    
    return answer

"""
설명
1. 배열에 있는 폰켄몬들을 키로 하고, 폰켄몬 개수를 value로하는 a_dic 생성(해시)
2. 최대로 고를 수 있는 가짓수는 배열의 크기/2, 키가 존재한다->적어도 그 종류의 폰켄몬이 하나이상 존재 하므로
최대 가짓수로 뽑으려면 무조건 하나로 뽑아야 되니, 뽑아야 되는 최대 가짓수 = 키의 개수로 보고
키의 개수가 max_choice보다 클 때는 mac_choice보다 적게 뽑야야 되니 return을 max_choice로
그 외엔 키의 개수로...

"""

""" 완주하지 못한 선수 문제"""
def solution(participant, completion):
    p_dic={}
    answer=""
    
    for i in participant:
        if i in p_dic :
            p_dic[i]+=1
        else:
            p_dic[i]=1
    
    for i in completion:
        p_dic[i]-=1
    
    for i in p_dic:
        if p_dic[i] !=0:
            return i
"""
설명
participant 의 사람명을 키로하고 사람수를 value로하는 dic만들고
completion의 명단에 있으면 사람수를 빼준다
0이 아니면 completion에 없었단 소리 -> return
""" 


"""전화번호 목록 문제"""

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

"""
설명
일단 리스트를 정렬해준다. 사전순으로 정렬
for문으로 돌면서 길이작은 순,사전 순으로 정렬되어있을거니
차례차례 올라가면서 비교만 해주면 되므로 반복문 한번당 인접두개의 요소에 접근하여
슬라이싱 이용해서 접두부분이 같은지 비교

"""

"""의상 문제"""

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










