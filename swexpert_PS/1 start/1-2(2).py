#1-2강 bitprint 함수 활용
def bitprint(i):
    for j in range(11, 0, -1):
        if (i&(1<<j)):
            print('1', end = '\n')
            i = i & ~(1<<j)
            print(i)
        else:
            print('0', end = '')
        

T = int(input())
for test_case in range(1, T+1):
    a = float(input())
    print('#%d' %test_case, end=' ')

    if a % 2**(-12) != 0:
        print('overflow')
    else:
        a = int(a*10**12)
        bitprint(a)
        print('', end='\n')