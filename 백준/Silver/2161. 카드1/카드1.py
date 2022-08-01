N = int(input())
queue = list(range(1, N + 1))

while len(queue) > 1:
    print(queue.pop(0), end=" ")
    queue.append(queue.pop(0))

print(queue[0])