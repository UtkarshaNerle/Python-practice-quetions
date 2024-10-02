c = ['hi','90','hello',50,40]
d = []
i = 0
while i < len(c):
    if type(c[i]) == str:
        d = d+[c[i]]
    i+=1
print(d)