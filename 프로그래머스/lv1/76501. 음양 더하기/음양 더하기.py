def solution(absolutes, signs):
    for i in range(len(signs)):
        if signs[i] == True:
            absolutes[i] = absolutes[i]
        else:
            absolutes[i] = -absolutes[i]
    
    answer = sum(absolutes)
    
    return answer