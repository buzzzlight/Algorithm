N = int(input())
list_ = list(map(int, input().split()))
list_ = sorted(list_)

print(list_[N//2])