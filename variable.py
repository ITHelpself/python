foo = 1
def func():
    bar = 2
    print(globals().keys())
    print(locals().keys())
func()
