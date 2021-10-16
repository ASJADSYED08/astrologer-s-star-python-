n=int(input("Enter Num=>"))
b=bool(int(input("INPUT 1 | 0 =>")))
if b==True:
    i=1
    while(i<=n):
        print("*"*i)
        i=i+1
elif b==False:
    i=n
    while(i>0):
        print("*"*i)
        i=i-1