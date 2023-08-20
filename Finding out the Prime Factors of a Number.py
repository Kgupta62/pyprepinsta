# Method 1: Using Simple Iteration
def fact(n):
    if n<4:
        return n
    arr=[]
    while n>1:
        for i in range(2,int(2+n//2)):
            if i==(1+n//2):
                arr.append(n)
                n=n//n
            if n%i==0:
                arr.append(i)
                n=n//i
                break
    return arr
n=210
print(fact(n))
# Method 2: Using Recursive Function
def Prime_Factorial(n, arr):
    if n < 4:
        return n
    for i in range(2, int(2+n//2)):
        if i == (1 + n // 2):
            arr.append(n)
            n = 1
            return
        if n % i == 0:
            arr.append(i)
            n = n // i
            Prime_Factorial(n, arr)
            break
    return arr


n = 210
arr = []
print(Prime_Factorial(n, arr))