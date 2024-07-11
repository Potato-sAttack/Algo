from functools import cmp_to_key

def compare(x, y):
    if x + y < y + x:
        return 1
    else:
        return -1

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(numbers)
    if answer[0] == '0':
        answer = '0'
    return answer