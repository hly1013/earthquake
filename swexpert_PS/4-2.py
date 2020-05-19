def partition(A, l, r):
    p = A[l]
    i = l+1
    j = r
    while i <= j:
        while(i <= j and A[i] <= p) : i += 1
        while(i <= j and A[j] >= p) : j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
    A[l], A[j] = A[j], A[l]
    return j

def quickSort(A, l, r):
    if l < r:
        s = partition(A, l, r)
        quickSort(A, l, s-1)
        quickSort(A, s+1, r)

'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    n = int(input()) 

    # n개의 경우에 대해 a 저장
    a = list(input().split())
    a = list(map(int, a))

    quickSort(a, 0, n-1)

    print('#%d %d' %(test_case, a[n//2]))