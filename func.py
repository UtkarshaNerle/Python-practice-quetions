a = 50
def b():
    global b
    b = 30
    print(b*a)
b()
print(a)