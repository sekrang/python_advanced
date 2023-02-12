"""
Chapter3 Advanced(3) - Descriptor(1)
Keyword - descriptor, set, get, del, property

"""
"""
descriptor
1. 객체에서 서로다른 객체를 속성값으로 가지는 것
2. Read, write, Delete 등을 미리 정의 가능
3. Data Descriptor(set, del), non-data descriptor(get)
4. 읽기 전용 객체 생성 장점, 클래스를 의도하는 방향으로

"""

# ex-1
# 기본적인 Descriptor 예제
class DescriptorEx1(object):
    def __init__(self, name = 'Default'):
        self.name = name
    
    def __get__(self, obj, objtype):
        return 'Get method called. -> self : {}, obj : {}, objtype : {}, name : {}'.format(self, obj, objtype, self.name)

    def __set__(self, obj, name):
        print('Set method called.')
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError('Name should be string')

        
    def __delete__(self, obj):
        print('Delete method called.')
        self.name = None

class Sample1(object):
    name = DescriptorEx1()

s1 = Sample1()

# Set 호출
s1.name = 'Descriptor Test1'

# 예외 발생
# s1.name = 10

# attr 확인
# Get 호출
print('ex-1 > ', s1.name)

# Delete 호출
del s1.name

# 재확인
# Get 호출
print('ex-1 > ', s1.name)
print()

# ex-2
# Property 클래스 사용 Descriptor 직접 구현
# class Property(fget = None, fset = None, fdel = None, doc = None)
class DescriptorEx2():
    def __init__(self, value):
        self. _name = value

    def getVal(self):
        return 'Get method called. -> self : {}, name : {}'.format(self, self._name)

    def setVal(self, value):
        print('Set method called.')
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError('Name should be string.')

    def delVal(self):
        print('Delete method called.')
        self._name = None

    name = property(getVal, setVal, delVal, 'Property method Example')

s2 = DescriptorEx2('Desciptor Test2')

# 최초 값 확인
print('ex-2 > ', s2.name)

# setVal 호출
s2.name = 'Descriptor Test2 method'

# 예외 발생
# s2.name = 10

# getVal 호출
print('ex-2 > ', s2.name)

# delVal 호출
del s2.name

# 재확인
# getVal 호출
print('ex-2 > ', s2.name)

# Doc 확인
print('ex-2 > ', DescriptorEx2.name.__doc__)