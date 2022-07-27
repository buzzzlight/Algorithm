N = int(input())

# 1부터 N 사이의 모든 수의 분해합 탐색
for number in range(1, N):
    # 분해합 저장 변수
    split_sum = 0

    # 각 자리수의 합 + 원래 숫자
    for digit in str(number):
        split_sum += int(digit)
    split_sum = split_sum + number

    # 분해합과 입력 N이 같으면 number는 N의 생성자
    if N == split_sum:
        print(number)
        break # 가장 작은 생성자를 만나면 break

# 생성자가 없을 경우
else:
    print(0)