def solution(s):
    answer = []
    
    for i in range(len(s)):
        if i == 0:
            answer.append(-1)
        elif i > 0:
            same = []
            for j in range(i):
                if s[j] == s[i]:
                    same.append(i-j)
            if same:
                answer.append(min(same))
            else:
                answer.append(-1)
            
    return answer