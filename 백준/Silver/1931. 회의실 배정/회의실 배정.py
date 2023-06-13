n = int(input())
time = []

for _ in range(n):
    start, end = map(int, input().split())
    time.append((start, end))

time.sort(key=lambda x: (x[1], x[0]))  # 끝나는시간으로 정렬한 다음 시작시간으로 정렬

cnt = 0
end_time = 0

for i in time:
    start, end = i

    if start >= end_time: # 시작시간이 끝나는시간보다 크거나 같다면
        cnt += 1
        end_time = end

print(cnt)