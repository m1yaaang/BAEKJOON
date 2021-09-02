#백준 5002 도어맨 실버1

X = int(input()) #기억할 수 있는 남녀차의 최대값
visitors = input() #입장
check = list(visitors)

M,W = 0,0 #남자,여자

for i in range(len(check)):
    if abs(M-W) < X: #기억할 수 있는 남녀차를 초과하지 않으면
        if check[i] == 'W':
            W += 1
        else:
            M += 1
    
    else:
        if M > W: #남자가 더 많으면
            if check[i] == 'M':
                if check[i+1] == 'M':
                    break
                elif check[i+1] == 'W':
                    temp = ''
                    check[i] = temp
                    check[i] = check[i+1]
                    check[i+1] = temp
                    W += 1
            elif check[i] == 'W':
                W += 1
        if W > M: #여자가 더 많으면
            if check[i] == 'W':
                if check[i+1] == 'W':
                    break
                elif check[i+1] == 'M':
                    temp = ''
                    check[i] = temp
                    check[i] = check[i+1]
                    check[i+1] = temp
                    M += 1
            elif check[i] == 'M':
                M += 1

V = M + W #총손님

print(V)


