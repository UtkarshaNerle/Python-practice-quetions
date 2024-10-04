m,n = 12,34
def outer_fun():
    p,q = 1,2
    print(m,n)
    print(p,q)
    def inner_fun():
        p = 4
        print(p,q)
        print(m,n)
    inner_fun()
    print(p,q)
print(m,n)
outer_fun()
print(m,n)