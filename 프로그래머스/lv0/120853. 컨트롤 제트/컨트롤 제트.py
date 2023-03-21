def solution(s):
    numbers = list(s.split())
    answer = 0
                   
    for i in range(len(numbers)):
        if numbers[i] != "Z":
            answer += int(numbers[i])
        else:
            answer -= int(numbers[i-1])

    return answer