# 백준 1303 전쟁-전투 실버1 - 푸는 중

# N명의 인접은 N^2의 위력, 대각선은 인접으로 보지 않음

import sys
import collections
input = sys.stdin.readline

N,M = map(int,input().split()) # 전쟁터 가로 N * 세로 M
field = [[]for _ in range(M)]
BP, WP = 0,0
move = [[0,1],[0,-1],[1,0],[-1,0]] # 가로세로 어떻게 해서 풀었던 것 같은데.. 

def bfs(color):
    q = collections.deque()
    visited = [[0 for _ in range(N)]for _ in range(M)] #방문 여부
    cnt = 0 #병사인원
    q.append((0,0))
    
    while q:
        if(field[i][j]==color):
            visited[i][j] = 1
        q.append(s)



for i in range(M):
    soldier = input() 
    for j in range(N):
        field[i][j]=soldier[j]




#연결된 병사를 각각 리스트로 출력
