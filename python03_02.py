"""
Chapter3 Advanced(3) - Meta Class(2)
Keyword - Type(name, base, dct), Dynamic metaclass

"""
"""
메타 클래스
1. 메타 클래스 동적 생성 중요
2. 동적 생성한 메타 클래스 -> 커스텀 메타 클래스 생성
3. 의도하는 방향으로 직접 클래스 생성에 관여 할 수 있는 큰 장점


"""

# ex-1
# type 동적 클래스 생성 예제

# Name(이름), Bases(상속), Dct(속성, 메소드)

class Sample1():
    pass

s1 = type('Sample1', (), {}) # 위에 것과 같음

print('ex-1 > ', s1)
print('ex-1 > ', type(s1))
print('ex-1 > ', s1.__base__)
print('ex-1 > ', s1.__dict__)

# ex-2
# 동적 생성 + 상속
class Parent1():
    pass

class Sample2(Parent1):
    attr1 = 100
    attr2 = 'hi'

s2 = type('Sample2', (Parent1,), dict(attr1 = 100, attr2 = 'hi')) # 위에 것과 같음

print('ex-2 > ', s2)
print('ex-2 > ', type(s2))
print('ex-2 > ', s2.__base__)
print('ex-2 > ', s2.__dict__)
print('ex-2 > ', s2.attr1, s2.attr2)

print()

# ex-2
# type 동적 클래스 생성 + 메소드

class SampleEx():
    attr1 = 30
    attr2 = 100

    def add(self, m, n):
        return m + n

    def mul(self, m, n):
        return m * n

ex = SampleEx()

print('ex-3 > ', ex.attr1)
print('ex-3 > ', ex.attr2)
print('ex-3 > ', ex.add(100, 200))
print('ex-3 > ', ex.mul(100, 20))

print()

s3 = type(
    'Sample3', 
    (object, ), 
    dict(attr1 = 30, attr2 = 100, add = lambda m, n: m + n, mul = lambda m, n: m * n)
    # {'attr1': 30, 'attr2': 100, 'add': lambda m, n: m + n, 'mul': lambda m, n: m * n}
    )
    
print('ex-3 > ', s3.attr1)
print('ex-3 > ', s3.attr2)
print('ex-3 > ', s3.add(100, 200))
print('ex-3 > ', s3.mul(100, 20))
