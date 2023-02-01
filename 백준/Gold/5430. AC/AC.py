import sys
from collections import deque

T = int(input())

for _ in range(T):
    ord = input()
    n = int(input())
    numbers = input()

    numbers = deque(numbers[1:-1].split(','))
    cnt_R = 0

    if n == 0:
        numbers = deque()
    
    for i in ord:
        if i == 'R':
            cnt_R += 1
        elif i == 'D':
            if numbers:
                if cnt_R % 2 == 0:
                    numbers.popleft()
                else:
                    numbers.pop()
            else:
                print('error')
                break
    else:
        if cnt_R % 2 == 0:
            print('[' + ','.join(numbers) + ']')
        else:
            numbers.reverse()
            print('[' + ','.join(numbers) + ']')