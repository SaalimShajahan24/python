a=int(input("enter 1st num: "))
b=int(input("enter 2nd num: "))

c=input("enter +,-,*,/  :  ")
if c=='+':
 res=a+b
elif c=='-':
 res=a-b
elif c=='*':
 res=a*b
elif c=='/':
 res=a/b
else:
 print("invalid operation")
print(res)
