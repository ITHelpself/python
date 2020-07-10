X = "hi"
def counter():
    num = 0
    def increment():
        global X
        X = "hello"
        nonlocal num
        num+=1
        return num
    return increment
c = counter()
c()
c()
c()
print(c())
print(X)