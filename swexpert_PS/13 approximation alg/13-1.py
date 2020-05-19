'''
T와 T_end, k가 정해졌을 때 새로운 비용을 구하는 cost()의 반복 횟수를 계산하는 프로그램을 만드시오.

[입력]
첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
다음 줄부터 테스트 케이스의 별로 T, T_end, k가 주어진다.
1<=T<=10000,  0＜T_end＜= 1,  0.8 ＜= k ＜ 1

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 테스트 케이스에 대한 답을 출력한다.
'''
# 답은 맞는데 runtime error가 뜨네...

import random
import math

def cost():
    global cnt

    cost_new = random.uniform(1, 10000)
    cnt += 1

    return cost_new


T = int(input())
for test_case in range(1, T + 1):
    T, T_end, k = map(float, input().split())

    cnt = 0
    cost_pre = math.inf  # 이전 비용

    while T > T_end:          # T_end가 될 때까지 반복
        cost_new = cost()      # 비용 계산
        diff = cost_new - cost_pre    # 새로운 비용과 이전 비용의 차이

        if diff < 0 or  math.exp(-diff/T) > random.random():
            cost_pre = cost_new    # 비용이 감소하거나 확률이 랜덤 값보다 더 크면 비용 갱신

        T = T*k                 # k : cooling factor

    print('#%d %d' %(test_case, cnt))