#Method 1 (Iterative)
num=6
fac=1
if num<=0:
    print("bhaiya possible ni hai smjho yr,ky kr rhe ho lala!")
else:
    for i in range(1,num+1):
        fac=fac*i
print(fac)

#Method 2 (Recursive)
def fact(num):
    if num==0:
        return 1
    return num*fact(num-1)
num=6
fac=fact(num)
print(fac)
