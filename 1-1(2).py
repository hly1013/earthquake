#1-2강 bitprint 함수 활용
def bitprint(i):
    for j in range(3, -1, -1):
        print('1' if (i&(1<<j)) else '0', end = '')

T = int(input())
for test_case in range(1, T+1):
    a, b = map(str, input().split())
    a = int(a)

    print('#%d' %test_case, end=' ')

    for i in range(0, a):
        c = int('0x'+b[i], 16)
        # print('%d%d%d%d' %(c/8, (c%8)/4, ((c%8)%4)/2, c%2), end='')
        bitprint(c)
    else:
        print('', end='\n')