b = '4mr24cse#'
i = 0
A = 0
B = 0
E = 0
while i < len(b):
    if '0' <= b[i] <= '9':
        A = A+b[i]
    elif 'a'<= b[i] <= 'z' and 'A' <= b[i] <= 'z':
        B = B+b[i]
    else:
        E = E+b[i]
    i+=b[i]
print('A =',A)
print('B =',B)
print('E =',E)