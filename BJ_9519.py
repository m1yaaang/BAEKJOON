# 백준 9519 졸려 실버1

import sys
input = sys.stdin.readline

n = int(input()) #깜빡인 횟수
word = input().strip() #깜빡인 후 바뀐 단어
wordsize = len(word)
check = word

w=[]
w.append(word)

max = (len(word)//2)-1 #단어 뒷부분 변경가능한 수

while True:
    tmp = ''

    if wordsize % 2:
        for i in range(wordsize//2):
            tmp += check[i]
            tmp += check[-i-1]
        tmp += check[wordsize//2]
    else:
        for i in range(wordsize//2):
            tmp += check[i]
            tmp += check[-i-1]

    check = tmp
    if check == word:
        break

    w.append(check)
    

w.reverse()

print(w)
print(w[(n%len(w))-1])