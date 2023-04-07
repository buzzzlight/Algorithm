n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

cards.sort()

def binary_search(num):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if cards[mid] == num:
            return 1
        elif cards[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for num in cards2:
    print(binary_search(num), end=' ')