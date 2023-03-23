def solution(n):
    answer = []
    n = list(str(n))
    for _ in range(len(n)):
        answer.append(int(n.pop()))
    
    return answer