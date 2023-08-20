# Method 1 : Using Brute Force
num = int(input("Enter a number to check even or odd:"))
if num%2==0:
    print("number is even.")
else:
    print("number is odd.")

# Method 2 : Using Ternary Operator
print("even") if num%2==0 else print("odd")

# Method 3 : Using Bitwise Operators
def isEven(num):
    return not num&1
if __name__=='__main__':
    if isEven(num):
        print("even")
    else:
        print("odd")
    print(14 & 1) #important (something new)

