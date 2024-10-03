d = ['hello','python','hi']
f = []
for i in d:
    c =0
    for j in i:
        if j in 'aeiouAEIOU':
            c = c+1
    f = f + [c]
print(f)