"""
Chapter1 Advanced(1) - Lambda, Reduce, Map, Filter Functions
Keyword - lambda, map, filter, reduce

"""
"""
lambda 장점 : 익명, 힘 영역 사용 즉시 소멸, pythonic?, 파이썬 가비지 컬렉션(Count=0)
일반 함수 : 재사용성 위해 메모리 저장
시퀀스형 전처리에 Reduce, Map, Filter 주로 사용

"""

# ex-1 lambda
cul = lambda a, b, c: a * b + c

print('ex-1 > ', cul(10, 15, 20))

# ex-2 map
digits1 = [x * 10 for x in range(1, 11)]
print('ex-2 > ', digits1)

result = list(map(lambda i: i ** 2, digits1))
print('ex-2 > ', result)

def also_square(nums):
    def double(x):
        return x ** 2
    return map(double, nums)

print('ex-2 > ', list(also_square(digits1)))

# ex-3 filter
digits2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, digits2))

print('ex-3 > ', result)

def also_even(nums):
    def is_even(x):
        return x % 2 == 0
    return filter(is_even, nums)

print('ex-3 > ', list(also_even(digits2)))

# ex-4 reduce
from functools import reduce

digits3 = [x for x in range(1, 101)]

result = reduce(lambda x, y: x + y, digits3)
print('ex-4 > ', result)

def also_add(nums):
    def add_plus(x, y):
        return x + y
    return reduce(add_plus, nums)

print('ex-4 > ', also_add(digits3))
































