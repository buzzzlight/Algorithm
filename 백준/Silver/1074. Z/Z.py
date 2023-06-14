n, r, c = map(int, input().split())


def Z(n, r, c):
    if n == 0:  # 한칸짜리일 경우
        return 0

    mid = 2 ** (n - 1)  # 중간점

    if r < mid and c < mid:  # 1사분면에 있을 경우
        return Z(n - 1, r, c)
    elif r < mid and c >= mid:  # 2사분면에 있을 경우
        return mid**2 + Z(n - 1, r, c - mid)
    elif r >= mid and c < mid:  # 3사분면에 있을 경우
        return 2 * (mid**2) + Z(n - 1, r - mid, c)
    else:  # 4사분면에 있을 경우
        return 3 * (mid**2) + Z(n - 1, r - mid, c - mid)


print(Z(n, r, c))