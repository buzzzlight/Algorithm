T = int(input())

for i in range(T):
    n, word = input().split()
    print(word[:int(n)-1], word[int(n):], sep='')