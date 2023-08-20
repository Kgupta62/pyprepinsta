# Method 1: Using Simple Iteration
num=10
n1,n2=0,1
print(n1,n2,end=" ")
for i in range(2,num):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=" ")
print()
# Method 2: Using Recursive Function
def fib(i):
    if i<=1:
        return i
    else:
        return fib(i-1)+fib(i-2)
num=10
if num<=0:
    print("bhai positive number dedeyrr")
else:
    print("babes your series:",end=" ")
    for i in range(num):
        print(fib(i),end=" ")
# Method 3: Using direct formulae
#don't follow this plzz
import math
def fibonacciSeries(phi, n):
    for i in range(0, n + 1):
        result = round(pow(phi, i) / math.sqrt(5))
        print(result, end=" ")
num = 10
phi = (1 + math.sqrt(5)) / 2
fibonacciSeries(phi, num)