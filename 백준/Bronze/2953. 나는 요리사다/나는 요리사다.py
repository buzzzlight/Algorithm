sum_ = []

# 총 합
for i in range(5):
    sum_.append(sum(map(int, input().split())))

# 총 합이 가장 높은사람의 인덱스 위치에 + 1
print(sum_.index(max(sum_)) + 1, max(sum_))