'''
파이썬의 라이브러리를 활용한 순열:
import itertools
mylist = [1, 2, 3]
result = itertools.permutations(mylist) #(mylist, 3)
				# r 생략시 기본값 리스트크기
print(list(result))
'''
import itertools
def perm(a):
    result = itertools.permutations(a)
    return(list(result))