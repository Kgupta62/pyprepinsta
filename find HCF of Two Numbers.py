# Method 1: Linear Quest to find HCF
num1 = 36
num2 = 60
hcf = 1
for i in range(1,min(num1,num2)):
    if num1%i ==0 and num2%i==0:
        hcf=i
print(hcf)
# Method 2: Euclidean Algorithm: Repeated Subtraction
num1 = 36
num2 = 90
while num1!=num2:
    if num1>num2:
        num1-=num2
    else:
        num2-=num1
print(num1)
# Method 3: Recursive Euclidean Algorithm: Repeated Subtraction
def hcf(num1,num2):
    if num1==0 or num2==0:
        return num1+num2
    if num1==num2:
        return num1
    if num1>num2:
        return hcf(num1-num2,num2)
    else:
        return hcf(num1,num2-num1)
num1 = 36
num2 = 60
print(hcf(num1,num2))
# Method 4: Modulo Recursive Euclidean Algorithm: Repeated Subtraction
def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)
num1 = 36
num2 = 60
print("Hcf of", num1, "and", num2, "is", getHCF(num1, num2))
