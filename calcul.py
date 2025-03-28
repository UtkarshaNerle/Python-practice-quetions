def calculator(a,b,operation):
    if operation == "add":
        print(a+b)
    elif operation == "sub":
        print(a-b)
    elif operation == "mul":
        print(a*b)
    elif operation =="div":
        if b==0:
            print ("error")
        return a/b
    else:
        print("invalide")

num1=float(input("enter value 1st = "))
num2=float(input("enter value 2nd = "))
operation = input("Enter operation (add/sub/mul/div): ")
calculator(num1,num2,operation)