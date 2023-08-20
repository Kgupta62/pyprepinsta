# Method 1 : Using [1, number] as the range
def div(n):
    i=1
    while i<=n:
        if (n%i==0):
            print(i,end=" ")
        i=i+1

div(100)
