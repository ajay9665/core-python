# calculatore

a=int(input("enter number="))
b=int(input("ente number="))
operator=input("enter any operator(+,-,*,/)")
if operator=='+':
    print("addition=",a+b)
elif operator =='-':
    print("substraction=",a-b)
elif operator =='*':
    print("mult",a*b)
elif operator =='/':
    print("division=",a/b)
else:
    print("invalid syntex")
