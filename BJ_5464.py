# 백준 5464 주차장 실버2

from collections import deque


def carIn(car):
    #자리가 없으면
    if 0 not in d:
        wait.append(car) #대기줄에 넣기

    #자리가 있으면
    else: 
        for i in range(N):
            if d[i] == 0: #빈자리가 있으면
                if car < 0:
                    d[i]=wait.popleft()#차량을 뺐을 경우에는 대기차량 주차
                else:
                    d[i] = car #자리에 차량 넣기
                break


N,M = map(int,input().split()) # 주차공간 N, 차량수 M
fee_w = [] # 주차공간 N개의 무게당 요금
weight = [] # 차량수 M개의 무게
fee = 0 # 총 수입
wait = deque()
d = [0 for _ in range(N)]

for i in range(N): #무게당 요금 입력받기
    fee_w.append(int(input()))

for i in range(M): #차량의 무게 입력받기
    weight.append(int(input()))

for i in range(2*M):
    record = int(input()) #차량 출입기록
    if record > 0:
        carIn(record)
            
    elif record < 0:
        loc = d.index(-1*record)
        if len(wait) > 0:
            d[loc] = 0
            carIn(record)
        else:
            d[loc] = 0

            
        fee += fee_w[loc]*weight[(-1*record)-1] #나갈 때 계산

print(fee)

