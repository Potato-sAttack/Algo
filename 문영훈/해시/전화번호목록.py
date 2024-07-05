"""전화번호 목록 문제(7/4)"""

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