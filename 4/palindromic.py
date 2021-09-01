from progress.bar import Bar

bar = Bar("progress" , max=99*99)
def ispalindrome(x):
    reverse = ""
    for i in range(len(x)-1,-1,-1):
        reverse+= x[i]
    if(reverse == x):
        return(True)
    return False

maxi = 0

palindromes = []
for i in range(900 , 999):
    for j in range(900 , 999):
        prod = i*j
        bar.next()
        if(ispalindrome(str(prod))):
            palindromes.append(prod)

print("\n result: \n")
print(max(palindromes))
