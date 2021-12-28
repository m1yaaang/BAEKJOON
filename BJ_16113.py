#백준 16113 시그널 실버2 문자열

import sys
input= sys.stdin.readline

#시그널의 총 길이는 항상 5의 배수(=행이 5개)
#숫자와 숫자 사이에는 1열 이상의 공백 존재(첫번째와 마지막 숫자 앞뒤에는 공백 X)
#숫자는 3열을 차지, 숫자 1은 다른 숫자와 다르게 1열 차지

#열로 배열을 만들어서 열이 공백인 부분 제외

N = int(input()) #시그널의 길이
AllOfSignal = input() 
col = N//5 #시그널의 column, row는 언제나 5

signal = [[0 for _ in range(5)]for _ in range(col)] #열을 기준으로 시그널 배열 생성(공백으로 숫자 구분)
tmp = 0
ans = ''

for i in range(5):
    for j in range(col):
        if(AllOfSignal[tmp]=='#'):
            signal[j][i]=1
        else:
            signal[j][i]=0
        tmp+=1

emptyRule = [0,0,0,0,0]

z = 0
while(z<col):
    if(signal[z]==emptyRule): #공백
        z+=1
    elif(signal[z]==[1,1,1,1,1]): # 0,1,6,8
        if(z+1>=col):
            ans += '1'
            z+=2
        elif(signal[z+1] == emptyRule): # 1
            ans += '1'
            z+=2
        elif(signal[z+1]==[1,0,0,0,1]): #0
            ans += '0'
            z+=3
        elif(signal[z+2]==[1,0,1,1,1]): #6
            ans += '6'
            z+=3
        else: #8
            ans += '8'
            z+=3
    elif(signal[z]==[1,1,1,0,1]): #5,9
        if(signal[z+2]==[1,0,1,1,1]):
            ans += '5'
            z+=3
        else:
            ans += '9'
            z+=3
    elif(signal[z]==[1,0,1,1,1]): #2
        ans += '2'
        z+=3
    elif(signal[z]==[1,0,1,0,1]): #3
        ans += '3'
        z+=3
    elif(signal[z]==[1,1,1,0,0]): #4
        ans += '4'
        z+=3
    elif(signal[z]==[1,0,0,0,0]): #7
        ans += '7'
        z+=3

print(int(ans))

#<1번째 열>
#[1,1,1,1,1] => 0,1,6,8
#-> 2번째 열 [1,0,0,0,1] => 0, (앞뒤)공백 => 1,
#-> 3번째 열 [1,0,1,1,1] => 6, [1,1,1,1,1] => 8 
#[1,0,1,1,1] => 2
#[1,0,1,0,1] => 3
#[1,1,1,0,0] => 4
#[1,1,1,0,1] => 5,9
#->3번째 열 [1,0,1,1,1] => 5, [1,1,1,1,1] => 9
#[1,0,0,0,0] => 7