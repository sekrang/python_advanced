"""
Chapter 1
Python Advanced(1) - Python Variable Scope
keyword - scope, global, nonlocal, local, global...

"""

"""

전역 변수는 주로 변하지 않는 고정 값에 대하여 사용
지역 변수 사용 이유 : 지역변수는 함수 내에서 로직 해결에 국한, 소멸주기 : 함수 실행 해제 시 
전역변수를 지역내에서 수정되는 것은 권장하지 않음
"""

# ex-1
a = 10 # Global variable

def foo():
    # Read Globla variable
    print('ex-1 > ', a)

foo()

# Read global variable
print('ex-1 > ', a)

# ex-2
b = 20

def bar():
    b = 30 # Local variable
    print('ex-2 > ', b) # Read Local variable

bar()
print('ex-2 > ', b)

# ex-3
c = 40

def foobar():
    # c = c + 10
    # c = 10
    # c += 100
    print('ex-3 > ', c)

foobar()
print('ex-3 > ', c)


# ex-4
d = 50

def barfoo():
    global d
    d = 60
    d += 100
    print('ex-4 > ', d)

barfoo()
print('ex-4 > ', d)

# ex-5(중요)
def outer():
    e = 70
    def inner():
        nonlocal e # nonlocal을 사용해야 사용가능함
        e += 10
        print('ex-5 > ', e)
    return inner

in_test = outer() # Closure

in_test()
in_test()

# ex-6
def func(var):
    x = 10
    def printer():
        print('ex-6 > ', "Printer Func Inner")
    print('Func Inner', locals()) # 지역 전체 출력

func('Hi')

# ex-7
print('ex-7 > ', globals()) # 전역 전체 출력
globals()['test_variable'] = 100
print('ex-7 > ', globals())

# ex-8(지역 -> 전역 변수 생성)
for i in range(1, 10):
    for k in range(1, 10):
        globals()['{}단 출력_{}곱하기{}'.format(i, i, k)] = i * k

print(globals())


