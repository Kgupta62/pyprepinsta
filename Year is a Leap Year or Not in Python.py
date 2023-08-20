# Method 1: Using if-else statements 1
year=2000
if (year%400 ==0 ) or (year%4==0 and year%100!=0): #very important
    print("leap year")
else:
    print("sorry! this is not a leap year")