import bisect
# exercici de biseccio
def index(a, x):
    i = bisect.bisect_left(a, x)
    return i
        
a = [1,2,4,5]
print(index(a, 6))
print(index(a, 3))