z = [30,32,31,34]
y =[]
i = 0
while i <len(z):
    if i%2 != 1:
        y = y+[z[i]]
    i+=1
print(y)