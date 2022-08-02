N = int(input())

for i in range(N):
    r, e, c = list(map(int, input().split()))
    # r = 광고를 하지 않았을 때 수익 
    # e = 광고를 했을 때 수익 
    # c = 광고 비용

    # 광고수익 = e - c 를 r과 비교
    if e - c > r:
        print("advertise")
    elif e - c < r:
        print("do not advertise")
    else:
        print("does not matter")