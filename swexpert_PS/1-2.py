T = int(input())
for test_case in range(1, T+1):
    a = float(input())
    print('#%d' %test_case, end=' ')

    if a % 2**(-12) != 0:
        print('overflow')
    else:
        for i in range(1, 13):
            if a >= 2**(-i):
                print(1, end='')
                a = a-2**(-i)
            elif a == 0:
                break  
            else:
                print(0, end='')
        print('', end='\n')