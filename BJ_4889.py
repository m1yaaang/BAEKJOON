#백준 4889 안정적인 문자열 실버

from collections import deque
import sys
input = sys.stdin.readline


def stable(str):
    s = deque() #여는 괄호만 담는 스택
    cnt = 0
    for i in range(len(str)):
        if str[i] == '{':
            s.append(str[i])
        elif str[i] == '}':
            if len(str) == 0:
                cnt += 1
            else:
                

        if len(str) == 0: #여는 괄호가 없고
            if str[i] == '}': #첫번째가 닫는 괄호면
                cnt += 1 #연산 1 추가
            elif str[i] == '{'


        if str[i] == '{':
            s.append(str[i])
            if len(s) == 0:    
                if str[i] == '}':
            x = -1

    return cnt 

str = ''
n = 1


while str[0] != '-':
    str = input()
    count = stable(str)
    print('{}. {}'.format(n,count))
    n += 1