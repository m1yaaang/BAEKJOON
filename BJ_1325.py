# 백준 1325 효율적인 해킹 

import sys
import collections
input = sys.stdin.readline

def bfs(start):
    cnt = 1
    visited = [0 for _ in range(N+1)]
    visited[start] = 1
    queue = collections.deque([start])

    while queue:
        u=queue.popleft()
        for v in com[u]:
            if not visited[v]:
                queue.append(v)
                visited[v]=1
                cnt += 1
    return cnt

N, M = map(int,input().split()) # 컴퓨터 N, 관계 M
com = [[]for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split()) # 신뢰관계 a b(a가 b를 신뢰,b는 a를 해킹 가능)
    com[b].append(a) #b가 접근할 수 있는 리스트

results = []
max_cnt = 0
for i in range(1, N+1):
    cnt=bfs(i)
    if(cnt > max_cnt):
        max_cnt = cnt
    results.append([i,cnt])

for i, cnt in results:
    if cnt == max_cnt:
        print(i,end = ' ')