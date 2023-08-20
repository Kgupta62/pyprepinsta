#method1=using brute force
num=15
if num>0:
    print("number is positive.")
elif num==0:
    print("number is zero.")
else:
    print("number is negative.")
#method 2=using nested if-else statement
num=-15
if num>=0:
    if num==0:
        print("number is zero.")
    else:
        print("number is positive.")
else:
    print("number is negative.")
#method 3=using ternary operator
# Ternary Operator Syntax
# ( Condition ) ? ( if True : Action) : ( if False : Action) ;
num=15
print("positive" if num>=0 else "Negative" )