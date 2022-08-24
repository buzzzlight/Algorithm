# 6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기
n = int(input())

if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')