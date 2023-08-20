# Method 0: Using String Extraction method
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)
# Method 1: Using Brute Force
num = 12345
sum = 0

while num!=0:
    digit = int(num%10)
    sum += digit
    num = num/10
print(sum)
# Method 2: Using Recursion I
num, sum = 12345, 0
def findSum(num, sum):
    if num == 0:
        return sum
    digit = int(num % 10)
    sum += digit
    return findSum(num / 10, sum)
print(findSum(num, sum))
# Method 3: Using Recursion II
num = 12345
def findSum(num):
    if num == 0:
        return 0
    return int(num % 10) + findSum(num / 10)
print(findSum(num))
# Method 4: Using ASCII table
num, sum = 12345, 0
for i in range(len(str(num))):
    # ord methods helps with ASCII
    sum += ord(str(num)[i]) - 48
print(sum)
# Method 5: Using map(), sum() and strip methods
def getSum(n):
    num_string = str(n)
    list_of_number = list(map(int, num_string.strip()))
    print(list_of_number)
    return sum(list_of_number)
n = int(input("Enter the number: "))
print(getSum(n))
# Method 6: One Line recursive function
def sumDigits(n):
    return 0 if n == 0 else int(n % 10) + sumDigits(int(n / 10))
n = int(input("Enter the number: "))
print(sumDigits(n))
# Method 7 : The cool method
n = [int(d) for d in input("Enter the number : ")]
print("the sum of digits is : ", sum(n))