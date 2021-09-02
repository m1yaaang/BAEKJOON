#백준 9012 괄호 실버4

def vps(data):
    a=0
    for i in data:
        if i == '(':
            a += 1
        elif a>0:
            if i == ')':
                a -= 1
        else:
            a=1
            break

    if a == 0:
        op.append('YES')
    else:
        op.append('NO')


T = int(input()) #테스트데이터 개수 T
op = []



for _ in range(T):
    str = input()
    vps(str)

for i in op:
    print(i)