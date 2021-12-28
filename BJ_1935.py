#백준 1935 후위표기식2 실버3 스택

import sys
input = sys.stdin.readline

stack = []

N=int(input()) #피연산자 개수 N
txt = input() #후위표기식
opr = []
for i in range(N):
    opr.append(input().strip())

for i in txt.strip():
    if(i>="A" and i<="Z"):
        stack.append(int(opr[ord(i)-65]))
    else:
        y = stack.pop()
        x = stack.pop()
        if(i=='+'):
            ans = x+y
        elif(i=='-'):
            ans = x-y
        elif(i=='*'):
            ans = x*y
        elif(i=='/'):
            ans = x/y
        stack.append(ans)

print("%.2f" % stack.pop())
