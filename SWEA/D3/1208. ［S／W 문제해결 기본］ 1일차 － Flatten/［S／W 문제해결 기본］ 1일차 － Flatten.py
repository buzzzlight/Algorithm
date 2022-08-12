for i in range(1, 11):
    d = int(input())
    box = list(map(int, input().split()))
    for j in range(d):
        box[box.index(max(box))] -= 1
        box[box.index(min(box))] += 1        
        if max(box) - min(box) < 2:
            break
    print(f'#{i} {max(box) - min(box)}')