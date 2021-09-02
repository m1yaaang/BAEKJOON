#백준 15828 Router 실버4

from collections import deque
import sys
input = sys.stdin.readline

N = int(input()) #라우터 버퍼의 크기
R = 0 # 입력받을 패킷 초기화
s = deque(maxlen=N) # 큐 생성

while True:
    R = int(input())
    if R == -1:
        break
    elif R == 0:
        s.popleft()
    elif R > 0 and len(s)<N:
        s.append(R)
    
if len(s) == 0:
    print('empty')
else:
    while len(s) != 0:
        print(s.popleft(),end=' ')
