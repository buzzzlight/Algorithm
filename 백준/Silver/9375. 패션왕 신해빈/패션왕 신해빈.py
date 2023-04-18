t = int(input())

for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        name, category = input().split()
        if category in clothes:     # 딕셔너리에 카테고리가 존재하면
            clothes[category] += 1      # 카테고리 + 1
        else:       # 존재하지 않으면
            clothes[category] = 1   # 값 1로 추가

    ans = 1
    for i in clothes.values():  # clothes 딕셔너리의 값들 (리스트)
        ans *= (i + 1) # 안입는 경우가 있으므로 + 1
    
    print(ans - 1)  # 아무것도 안입는 경우를 빼줌