a =5
b = 20
def hello():
    b = 30
    global c
    c = b+a
    print(a)
hello()
print(b)
print(b)
print(c)