input = 'Roses are red'
b = ''  

for a in input:
    if a == ' ':  
        b= b+'_'  
    else:
        b= b+ a  
print(b)
