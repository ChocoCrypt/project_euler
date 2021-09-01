import numpy as np
def total_sum(n):
    total = 0
    #me lo pela esta identidad
    for i in range(1,n+1):
        total += np.power(i,2)
    return(total)

def total_square_sum(n):
    total = np.power((n*(n+1)/2) ,2)
    return(total)



def ejercicio(num):
    difference = total_square_sum(num) - total_sum(num)
    return(difference)


total = ejercicio(100)

print(total)
