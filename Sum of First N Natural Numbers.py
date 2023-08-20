# Method 1 : Using for Loop
num=5
sum=0
for i in range(num+1):
    sum+=i
print(sum)
# Method 2 : Using Formula for the Sum of Nth Term
print(int(num*(num+1)/2))
# Method 3 : Using Recursion
def getsum(num):
    if num==1:
        return 1
    return num + getsum(num-1)
print(getsum(num))