import math
#method1
low=10
high=1000
for n in range(low,high+1):
    length=len(str(n))
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**length
        temp//=10
    if n==sum:
        print(n,end=", ")
#Method 2
first=10
secound=1000
def arm(val):
    sum=0
    arr=[int(d) for d in str(val)]
    for i in range(len(arr)):
        sum+=math.pow(arr[i],len(arr))
    if sum==val:
        print(val,end=", ")
for i in range(first,secound+1):
    arm(i)

