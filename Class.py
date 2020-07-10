class A:
    pass
a = A()
a.x = 3
print(a.x)
del a.x
x = {'a':1, 'b':3}
del x['a']
class Fred:
    a = 'class'
    b = (a for i in range(10))
    c = [a for i in range(10)]
    d = a
    e = lambda: a
    f = lambda a = a:a
    @staticmethod
    def g():
        return a
print(Fred.a)
print(next(Fred.b))
print(Fred.c[0])
print(Fred.e())
print(Fred.f())
print(Fred.g())
class B:
    a = 42
    b = list(i for i in range(10))

