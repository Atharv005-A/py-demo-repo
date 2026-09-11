# # # # # # # # minutes=int(input("Enter the number of minutes: "))
# # # # # # # # print(f"{minutes} is  {minutes // 60} hours and {minutes % 60} minutes.")


# # # # # # # # num=int(input("enter number "))
# # # # # # # # print(f"{num}: last digit is {num%10}")


# # # # # # # role=input("Enter your role: ")
# # # # # # # role=role.lower()
# # # # # # # age=int(input("Enter your age: "))


# # # # # # # print("eligible:",bool(role=="student" and age<=21))









# # # # # # # a=10
# # # # # # # b=20
# # # # # # # print(f"before swap a={a} b={b}")
# # # # # # # a=a+b
# # # # # # # b=a-b
# # # # # # # a=a-b
# # # # # # # print(f"after swap a={a} b={b}")


# # # # # # # #version 1
# # # # # # # #hello
# # # # # # # #bye
# # # # # # # #one two





# # # # # # # condional statements
  

# # # # # # # is_raining=False
# # # # # # # if is_raining:
# # # # # # #     print("take umbrella")      
# # # # # # # else:
# # # # # # #     print("no need to take umbrella")


# # # # # # age=int(input("Enter your age: "))
# # # # # # if age>=18:
# # # # # #     print("eligible to vote")   
# # # # # # else:
# # # # # #     print("not eligible to vote")



# # # # # day=int(input("Enter the day number: "))
# # # # # if day==1:  
# # # # #     print("sunday")
# # # # # elif day==2:
# # # # #     print("monday")
# # # # # elif day==3:
# # # # #     print("tuesday")
# # # # # elif day==4:
# # # # #     print("wednesday")
# # # # # elif day==5:
# # # # #     print("thursday")
# # # # # elif day==6:
# # # # #     print("friday")
# # # # # elif day==7:
# # # # #     print("saturday")
# # # # # else:
# # # # #     print("invalid day number")




# # # # age=int(input("Enter your age: "))
# # # # has_id=True
# # # # if age>=18:
# # # #     if has_id:
# # # #         print("entry allowed")
# # # #     else:               
# # # #         print("entry denied: ID required")
# # # # else:
# # # #     print("underage")



# # # day=int(input("Enter the day number: "))

# # # match day:
# # #     case 1:
# # #         print("sunday")
# # #     case 2:
# # #         print("monday")
# # #     case 3:
# # #         print("tuesday")
# # #     case 4:
# # #         print("wednesday")
# # #     case 5:
# # #         print("thursday")
# # #     case 6:
# # #         print("friday")
# # #     case 7:
# # #         print("saturday")
# # #     case _:
# # #         print("invalid day number")






# # # num=int(input("Enter a number: "))


# # # if num%2==0:
# # #     print(f"{num} is even")
# # # else:
# # #     print(f"{num} is odd")




# # age=int(input("Enter your age: "))
# # prize=100

# # if age<=12:
# #     prize=prize-(prize/10)
# #     print(f" Prize is {prize}")
# # else:
# #     print(f"Prize is {prize}")




# score=int(input("enter your score:"))
# if score>100 or score<0:
#     print("incorrect score")

# elif score>=90:
#     print("garde is O")
# elif score>=80:
#     print("garde is A")
# elif  score>=65:
#     print("garde is B")
# elif score>=35:
#     print("garde is C")
# elif score<35:
#     print("fail")
# else:
#     print("wrong input")



num=int(input("enter any number"))
if num==0:
    print("zero or nuteral number")
elif num>0:
    print("postive number")
elif num<0:
    print("negative number")