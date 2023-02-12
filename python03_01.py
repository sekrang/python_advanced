"""
Chapter3 Advanced(3) - Meta Class(1)
Keyword - Class of Class, Type, Meta Class, Custom Meta Class

"""
"""
메타 클래스
1. 클래스를 만드는 역할 -> 의도하는 방향으로 클래스를 커스텀
2. 프레임워크 작성 시 필수
3. 동적 생성(type), 커스텀 생성(type) 함수
4. 커스텀 클래스 -> 검증 클래스등
5. 엄격한 Class 사용을 요구, 메소드 오버라이드 요구

"""

# ex-1
# type 에제
class SampleA(): # Class == Object
    pass

obj1 = SampleA() # 변수에 할당, 복사 가능, 새로운 속성 추가 가능, 함수의 인자로 넘기기 가능

# obk1 -> SampleA instance
# SampleA -> type meta class
# type -> type meta class
print('ex-1 > ', obj1.__class__)
print('ex-1 > ', type(obj1))
print('ex-1 > ', obj1.__class__ is type(obj1))

# type이 모든 클래스의 원형
print('ex-1 > ', obj1.__class__.__class__)
print('ex-1 > ', obj1.__class__.__class__ is type(obj1.__class__))

print(type.__class__) # 핵심

# ex-2
# type meta(ex-1 증명)

# int, dict
n = 10
d = {'a': 10, 'b': 20}

class SampleB():
    pass

obj2 = SampleB()

for o in (n, d, obj2):
    print('ex-2 > {} {} {}'.format(type(o), type(o) is o.__class__, o.__class__.__class__))
    print()

for t in int, float, list, tuple:
    print('ex-2 > ', type(t))

print()
print('ex-2 > ', type(type))