class a:
    vara = "welcome to class a"
class b:
    varb = "welcome to class b"
class c(a,b):
  varc = "welcome to class c"

c1 = c()

print(c1.varc)
print(c1.varb) 
print(c1.vara)   
 