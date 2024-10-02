b = 'ok! bye'
i =0
d = 0
while i < len(b):
    if b[i] in 'aeiouAEIOU':
        d +=1
    i+=1
print('d =',d)