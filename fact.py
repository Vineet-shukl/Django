def fact(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return -1
    else:
        return n * fact(n - 1)
x=int(input("Enter a number: "))
print(fact(x))