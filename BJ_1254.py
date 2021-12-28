#백준 1254 팰린드롬 만들기 실버1 - 푸는중

import sys
input = sys.stdin.readline

def ispalin(str,s,e):
    while(s<e):
        if(str[s] != str[e]):
            return False
            break
        s+=1
        e-=1
    return True


S=input().strip()

left = 0
right = len(S)-1
mid = (left+right)/2

if(S==S[::-1]):
    print(len(S))


# stack=[]

# for i in S:
#     stack.append(i)

# for i in range(len(stack)):
#     revS += stack[-i-1]

# cnt = -2

# # for i in range(len(S)-1):
# #     if(S == revS):
# #         break
# #     else:
# #         stack.append(S[cnt])
# #         S+=S[cnt]
# #         revS = ''
# #         for i in range(len(stack)):
# #             revS += stack[-i-1]
# #         cnt -= 2
# #         print("revS : %s, S : %s"%(revS,S))

# while(revS!=S and -cnt<=len(S)):
#     stack.append(S[cnt])
#     S+=S[cnt]
#     revS = ''
#     for i in range(len(stack)):
#         revS += stack[-i-1]
#     cnt -= 2
#     print("revS : %s, S : %s"%(revS,S))

# print(len(stack))


# 반례 eeeffe 8, sascsc 9, aabc 7, abcdba 11, sass 6  

# 부분 팰린드롬을 찾기

# 길이가 2 이상인 문자열이 들어올경우 그 문자가 대칭인지 확인합니다.
# 맞다면 그 길이를 리턴하고, 아니라면 가장 마지막 문자와 동일한 문자를 문자의 맨뒤 -1 인덱스부터 찾습니다 문자의 시작 인덱스부터 확인
# 찾은 해당 인덱스에서부터 마지막문자까지 대칭인지 확인합니다. ( 최악인경우 문자는 마지막 문자를 기준으로 대칭이 되기에 찾은 인덱스의 앞부분은 대칭으로 생각합니다.)
# 찾은 인덱스가 없거나 해당 인덱스에서 대칭이 아니라면 대칭이면 작업을 중단하고, 마지막 으로 대칭이였던 인덱스 번호 만큼 현재의 길이에 더해줍니다.
