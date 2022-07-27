word = input()
upper_word = word.upper()           # 모두 대문자로 바꾸기
alphabet = list(set(upper_word))     # 알파벳 중복값을 제거한 리스트 생성

count_list = []      # 알파벳 개수 합 리스트

# alphabet에 있는 i가 upper_word에서 몇개인지 셈
for i in alphabet:
    count = upper_word.count(i)
    count_list.append(count)

# 최대값이 두개 이상이라면 ? 출력
if count_list.count(max(count_list)) >= 2:
    print('?')

# 최대값이 하나라면 동일한 위치의 알파벳 출력
else:
    max_index = count_list.index(max(count_list))
    print(alphabet[max_index])