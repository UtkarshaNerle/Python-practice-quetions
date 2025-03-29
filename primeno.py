def prime(n):
    if n==1:
        return "not prime"
    for i in range (2,10):
        if n%i == 0:
            return "not prime"
    return "prime"
num = int(input("enter the value: "))
print(prime(num))    