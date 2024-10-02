b = [1,4,5,'2','1','3',11,7,'17']
i = 0
sum = 0
while i < len(b):
    if type(b[i]) == int:
        sum+=b[i]
    i+=1   
print([sum])

# B = [1, 4, 5, '2', '1', '3', 11, 7, '17']
# i = 0
# sum = 0
# while i < len(B):
#     if type(B[i]) == int:
#         sum = sum + B[i]
#     i += 1
# print([sum])       