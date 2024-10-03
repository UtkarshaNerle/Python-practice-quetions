input = ['hi','sql','bye','python','1+0j',7.8]
#o/p = ['hi','python']
b = []

for a in input:
    if type(a) == str:
        b+=1
print(b)