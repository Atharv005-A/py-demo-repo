num=int(input("enter any number for diigit count:"))
cnt=0
while num>1:
    num=num/10
    cnt=cnt+1
print(cnt)