'''
서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장한다. 그런 다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색을 통해 확인하려고 한다.
전체 탐색 구간의 시작과 끝 인덱스를 l과 r이라고 하면, 중심 원소의 인덱스 m=(l+r)//2 이고, 이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다.
이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는 숫자의 개수를 알아보려고 한다.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 A와 B에 속한 정수의 개수 N, M이 주어지고, 두 줄에 걸쳐 N개와 M개의 백만 이하의 양의 정수가 주어진다.
1<=N, M<=500,000

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
'''
# "양쪽 구간을 번갈아 선택"한다는 게 뭔지 모르겠네

def binarySearch(a, key):
    global left, right

    start = 0
    end = len(a)-1

    while start <= end:
        middle = start + (end-start)//2
        if key == a[middle]:
            return middle
        elif key < a[middle]:
            if start - end + 1 == 3:
                if key == a[end] : 
                    right += 1
                    return end
            end = middle-1
            right += 1
        else: 
            if start - end + 1 == 3:
                if key == a[start] : 
                    left += 1
                    return start          
            start = middle+1
            left += 1
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
        if (left - right <= 1) and (left - right >= -1) and (temp != -1):
            sum += 1

    print('#%d %d' %(test_case, sum))