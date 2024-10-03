i = "sp" 
j = ['sql','python']
d = {}
for a in i:
    for b in j:
        if a == b[0]:
            d[a] = b
print(d)