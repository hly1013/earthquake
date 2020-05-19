T = int(input())

DPL = {1:1, 2:3, 3:6}
def getDPL(k):
    if k-1 
    DPL[k] = DPL[k-1]*2*1 + DPL[k-2]*2*2 + DPL[n-3]*2*1

for test_case in range(1, T + 1):
    n = int(input())
    global DPL

    while (n in DPL) is not True:
        if n-3 in DPL:
            if n-2 in DPL:
                if n-1 in DPL:
                    getDPL(n)
                else:
                    getDPL(n-1)
            else:
                getDPL(n-2)
        else:
            getDPL(n-3)

