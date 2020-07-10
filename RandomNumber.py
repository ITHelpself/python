import random
def lottery(count,start, end):
    for i in range(count):
        yield random.randint(start,end)
count = 50
start = 4
end = 32
for i in lottery(count,start,end):
    print("random numbers: %d "% i)
