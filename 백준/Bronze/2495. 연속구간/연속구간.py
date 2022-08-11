for i in range(3):
    number = int(input())
    number = str(number)
    list_ = list(number)
    cnt = 1
    max = 1

    for j in range(7):
        if list_[j] == list_[j + 1]:
            cnt += 1
            if cnt > max:
                max = cnt
        else:
            if cnt > max:
                max = cnt
            cnt = 1

    print(max)