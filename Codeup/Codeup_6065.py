# 6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기

a, b, c = map(int, input().split())
list = [a, b, c]

for i in list:
    if i % 2 == 0:
        print(i)