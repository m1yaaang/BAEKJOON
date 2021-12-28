#백준 2841 외계인의 기타 연주 실버1 스택

import sys
input = sys.stdin.readline

#만약, 어떤 줄의 프렛을 여러 개 누르고 있다면, 가장 높은 프렛의 음이 발생한다.

N,P = map(int,input().split()) #멜로디의 음 N, 한 줄의 프렛 P
cnt = 0 #움직임
melody = []

line,fret=map(int,input().split()) #새로운 멜로디 음 line, 새로 누를 프렛 fret
melody.append(fret)
cnt += 1

for i in range(N-1):
    n,p=map(int,input().split()) #다음 멜로디 음 n, 다음 누를 프렛 p
    if(n==line):
        while(melody[-1]>p):
            melody.pop()
            cnt += 1
        if(melody[-1]!=p):
            melody.append(p)
            cnt += 1
    else:
        while(len(melody)==0):
            melody.pop()
            cnt += 1
        melody.append(p)
        cnt += 1
    line,fret = n,p
    print(melody)
    print("cnt >> %d"%cnt)

while(len(melody)!=0):
    melody.pop()
    cnt += 1

print(cnt)