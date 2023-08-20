# Method 1: Using Iteration
number=371
num=number
digit,sum=0,0
length=len(str(number))
for i in range(length):
    digit = int(num%10)
    num=num/10
    sum+=pow(digit,length)
if sum == number:
    print("Armstrong")
else:
    print("sorry")

#Using Recursion
number=371
num=number
sum=0
legth=len(str(num))
def check(num,legth,sum):
    if num==0:
        return sum
    sum+=pow(int(num%10),length)
    return check(num/10,length,sum)
if check(num,length,sum)==number:
    print("armstrong")
else:
    print("sorry")