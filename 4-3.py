def binarySearch(a, key):
    global left, right

    start = 0
    end = len(a)-1

    while start <= end:
        middle = start + (end-start)//2
        if key == a[middle]:
            right, left = 1, 1
            return middle
        elif key < a[middle]:
            if start - end + 1 == 3:
                if key == a[end] : 
                    right = 1
                    return end
            end = middle-1
            right = 1
        else: 
            if start - end + 1 == 3:
                if key == a[start] : 
                    left = 1
                    return start          
            start = middle+1
            left = 1
    return -1


'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    n, m = map(int, input().split())

    #A
    A = list(input().split())
    A = list(map(int, A))

    #B
    B = list(input().split())
    B = list(map(int, B))

    #sorting N (ascending order)
    A = sorted(A)

    sum = 0
    for i in range(0, m):
        left, right = 0, 0
        temp = binarySearch(A, B[i])
        if (left and right) and (temp != -1):
            sum += 1

    print('#%d %d' %(test_case, sum))