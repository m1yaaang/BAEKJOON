# 백준 20364 부동산다툼 실버2

import sys
input = sys.stdin.readline

N,Q = map(int,input().split()) #땅개수 N, 오리수 Q

m = [0 for _ in range(N+1)] #방문여부

for i in range(Q): 
    X = int(input()) #오리가 원하는 땅 X
    tmp = X
    res = 0 #방문가능 기본값
    while tmp > 1:  #땅까지 가는길 표시 위함
        if m[tmp] == 1: #방문했으면
            res = tmp #처음 마주치는 점유된 땅
        tmp = tmp >> 1 # 8->4->2->1
    print(res) #res를 계속 덮어쓰기 해서 최초 집 찾기
    if res == 0: #가는 길에 방문한 적 없으면
        m[X] = 1 #땅번호 체크