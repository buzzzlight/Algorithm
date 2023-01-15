T = int(input())

for i in range(T):
    stack = []
    vps = input()
    for j in vps:
        if j == '(':
            stack.append(j)
        if j == ')':
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else: # for-else break문으로 끊기지 않았을 경우 수행
        if len(stack) == 0:
            print('YES')
        else:
            print('NO')