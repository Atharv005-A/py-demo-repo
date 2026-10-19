def table(n):
    print("table of ",n,":")
    for i in range(1,11):
        print(n," * ",i,"=",n*i)

n=int(input("enter number for printing table:"))
table(n)