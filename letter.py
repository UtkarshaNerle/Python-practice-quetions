b = '4mr24cse#'
i = 0
A = ""
B = ""
E = ""
while i < len(b):
    if '0' <= b[i] <= '9':
        A = A+b[i]
    elif 'a'<= b[i] <= 'z' and 'A' <= b[i] <= 'z':
        B = B+b[i]
    else:
        E = E+b[i]
    i+=1
print('A (alphabetes) =',A)
print('B (numbers)=',B)
print('E (special charchar)=',E)         