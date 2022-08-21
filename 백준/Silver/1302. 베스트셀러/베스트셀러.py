N = int(input())
book = []

for i in range(N):
    book.append(str(input()))

book.sort()
book_set = list(set(book))
book_set.sort()
cnt_list = []

for i in book_set:
    cnt_list.append(book.count(i))

print(book_set[cnt_list.index(max(cnt_list))])