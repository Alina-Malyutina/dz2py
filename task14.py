N = int(input('Enter integer number greater than 1: '))
res = []
k=0
while 2**k < N:
    res.append(2**k)
    k += 1
print (res)