while True:
    tri = list(map(int, input().split()))
    tri.sort()

    if tri[0] == 0:
        break
    elif tri[0]**2 + tri[1]**2 == tri[2]**2:
        print('right')
    else:
        print('wrong')