N = int(input())
score = list(map(int, input().split()))

print(sum(score)/max(score)*100/N)