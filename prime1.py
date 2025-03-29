import math
def prime(n):
    if n<=1:
        return False
    for i in range (2,n):
        if n%i == 0:
            return False
    return True
for num in range(2,101):
    if prime(num):
        print(num, end=" ")    