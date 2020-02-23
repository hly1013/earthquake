T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    #2차원 리스트 생성
    l = [] #idx i, j: i->j 때의 소비량
    for i in range(0, n):
        l.append([])
        _input = input()
        temp = _input.split()
        for j in range(0, n):
            l[i].append(int(temp[j]))
    
    #배열 생성 확인
    for i in range(0, n):
        for j in range(0, n):
            print(l[i][j], end = ' ')
        print('')