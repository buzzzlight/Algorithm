# N = 리스트 길이
N = int(input())

# 높이 리스트 입력
road = list(map(int, input().split()))
# 누적 합 저장 변수
total = 0
# 누적 합 리스트
upp = []

# 오르막길을 찾기 위해 인덱싱
for i in range(1, len(road)):
    # 오르막길 = 현재 값 > 이전 값
    if road[i] > road[i - 1]:
        # 오르막길의 전체 길이는 부분 오르막길 길이의 누적 합
        total += road[i] - road[i - 1]
    # 오르막길이 아닐 경우
    else:
        upp.append(total)
        total = 0

# 마지막 누적 합 저장
upp.append(total)

if len(upp) == 0:
    print(0)
else:
    print(max(upp))