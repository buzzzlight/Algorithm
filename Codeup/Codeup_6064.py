# 6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기

a, b, c = map(int, input().split())

print((a if a < b else b) if ((a if a < b else b) < c) else c)