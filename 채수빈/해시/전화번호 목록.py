# phone_book = 전화번호 배열
# 접두어인 경우가 있으면 false

def solution(phone_book):
    dic = dict()
    
    # 전화번호 딕셔너리 생성
    for i in phone_book:
        dic[i] = 1
    
    for phone_number in phone_book:
        temp = ""
        # 전화번호 앞자리 부터 하나씩 temp에 추가하면서 번호가 존재하는지 확인
        for n in phone_number:
            temp += n
            # temp가 dic에 존재한다는 것은 다른 번호의 접두어라는 뜻 and 자기 자신 제외
            if temp in dic and temp != phone_number:    
                return False
    return True
    

# 효율성X
# def solution(phone_book):
#     for i in range(len(phone_book)):
#         for j in range(i+1, len(phone_book )):
#             if phone_book[i].startswith(phone_book[j]):
#                 return False
#             elif phone_book[j].startswith(phone_book[i]):
#                 return False
#     return True

# phone_book =  ["119", "97674223", "1195524421"]
# print(solution(phone_book))