def merge(left, right):
    result = []
    global case
    if left[-1] > right[-1]:
        case += 1

    while len(left) > 0 and len(right) > 0 :
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if len(left) > 0:
        result.extend(left)
    if len(right) > 0:
        result.extend(right)
    return result

def merge_sort(m):
    if len(m) <= 1:
        return m

    mid = len(m)//2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    n = int(input()) 

    case = 0        #두번째 출력값: 오른쪽 원소가 먼저 복사되는 경우의 수

    # n개의 경우에 대해 a 저장
    a = list(input().split())
    a = list(map(int, a))

    a = merge_sort(a)
    print('#%d %d %d' %(test_case, a[n//2], case))