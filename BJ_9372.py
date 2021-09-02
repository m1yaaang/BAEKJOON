#백준 9372번 상근이의 여행 실버4

from collections import deque
import sys
input = sys.stdin.readline

def bfs(a):
    q = deque()
    q.append(a)
    check[a] = 1
    cnt = 0
    while q:
        a = q.popleft()
        for i in node[a]:
            if check[i] == 0:
                check[i] = 1
                cnt += 1
                q.append(i)
    return cnt

T = int(input()) #테스트 케이스의 수

for _ in range(T):
    N,M = map(int,input().split()) #국가의 수 N, 비행기의 종류 M
    node = [[] for i in range(N+1)] #연결그래프
    check = [0 for i in range(N+1)] #방문여부 확인
    for _ in range(M):
        a,b = map(int,input().split()) #a와 b를 왕복하는 비행기 노선
        node[a].append(b)
        node[b].append(a)

    ans = 0
    print(check)
    for i in range(1,N+1):
        if check[i] == 0:
            ans += bfs(i)
    print(ans)


