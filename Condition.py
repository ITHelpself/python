a = 3
print("greater than 2" if a>2 else "smaller than 2")
x = 6
y = 2
def cmp(a,b):
    if a==b:
        return 0
    elif a>b:
        return 1
    else:
        return -1

a=["x equal than y","x great than y","x less than y"][cmp(x,y)]
print(a)