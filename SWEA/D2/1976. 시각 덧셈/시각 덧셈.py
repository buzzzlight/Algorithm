T = int(input())

for test_case in range(1, T + 1):
    H1, M1, H2, M2 = map(int, input().split())
    H = H1 + H2
    M = M1 + M2
    if M >= 60:
        M = M - 60
        H = H + 1
    if H > 12:
        H = H - 12
    print(f'#{test_case} {H} {M}')