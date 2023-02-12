N = int(input())
word = []

for _ in range(N):
    word.append(input())

word = list(set(word))
word.sort()
word.sort(key=lambda x:len(x))

for i in word:
    print(i)