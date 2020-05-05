'''
병합 정렬을 이용해 오름차순으로 정렬

N개의 정렬 대상을 가진 리스트 L
L[0:N//2], L[N//2:N]으로 분할
병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다.

정렬이 끝난 리스트 L
L[N//2] 원소를 출력

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 
1<=T<=50
다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어진다.
5<=N<=1,000,000
0 <= ai <= 1,000,000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,  N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수를 출력
'''

'''
merge function
'''
#항상 l이 r보다 길거나 같다
def merge(left, mid, right):
    global cnt, L, N, result

    i = left
    j = mid+1
    idx = left
    while i <= mid and j <= right:
        if L[i] < L[j]:
            result[idx] = L[i]
            i += 1
            idx += 1
        else:
            result[idx] = L[j]
            j += 1
            idx += 1
     #l과 r의 원소를 다 정렬하여 result로 냈다면 i == len(l), j == len(r)   
     # i < len(l) 혹은 j < len(r)라는 것은 다 정렬하지 못했다는 뜻
     #그러나 while loop를 나왔으므로 l, r 중 하나는 다 탐색한 것

    if i <= mid: #l을 다 탐색하지 못한 경우
        cnt += 1
        result[idx:right+1] = L[i:mid+1]
    if j <= right:
        result[idx:right+1] = L[j:right+1]

    print(result)

    for i in range(left, right+1):
        L[i] = result[i]


'''
merge sort function
'''
def merge_sort(left, right):
    if left < right:
        mid = (left+right)//2

        merge_sort(left, mid)
        merge_sort(mid+1, right)

        merge(left, mid, right)
  
'''
main function
'''
T = int(input())
for test_case in range(1, T+1):
    N = int(input()) 

    # 길이 N인 리스트 L
    L = list(input().split())
    L = list(map(int, L))

    cnt = 0
    result = [0]*N

    # idx: 0 ~ len(lst)//2, len(lst)//2+1 ~ len(lst)-1
    l = 0
    r = N - 1

    merge_sort(l, r) # merge(L[left:right//2], L[right//2+1:right])

    print('#%d %d %d' %(test_case, L[N//2], cnt))
    print(result)