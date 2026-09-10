# minutes=int(input("Enter the number of minutes: "))
# print(f"{minutes} is  {minutes // 60} hours and {minutes % 60} minutes.")


# num=int(input("enter number "))
# print(f"{num}: last digit is {num%10}")


role=input("Enter your role: ")
role=role.lower()
age=int(input("Enter your age: "))


print("eligible:",bool(role=="student" and age<=21))









a=10
b=20
print(f"before swap a={a} b={b}")
a=a+b
b=a-b
a=a-b
print(f"after swap a={a} b={b}")


#version 1
#hello