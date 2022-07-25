T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    a = W * P
    b = Q
    if W > R:
        b = Q + (W - R) * S
    
    if a > b:
        print(f'#{test_case} {b}')
    else:
        print(f'#{test_case} {a}')
    