T = int(input())
for test_case in range(1, T+1):
    a, b = map(str, input().split())
    a = int(a)

    print('#%d' %test_case, end=' ')

    for i in range(0, a):
        c = int('0x'+b[i], 16)
        print('%d%d%d%d' %(c/8, (c%8)/4, ((c%8)%4)/2, c%2), end='')
    else:
        print('', end='\n')