
fib = [1,1]

i = 2
num = 0
while(num < 4_000_000):
    fib.append(fib[i-1]+fib[i-2])
    num = fib[i-1] + fib[i-2]
    i+=1

pares = [x for x in fib if x%2 == 0]
res = sum(pares)
print(res)
