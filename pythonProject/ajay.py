# # calculatore
#
# a=int(input("enter number="))
# b=int(input("ente number="))
# operator=input("enter any operator(+,-,*,/)")
# if operator=='+':
#     print("addition=",a+b)
# elif operator =='-':
#     print("substraction=",a-b)
# elif operator =='*':
#     print("mult",a*b)
# elif operator =='/':
#     print("division=",a/b)
# else:
#     print("invalid syntex")
#
#



class Calc:
    def sum(self,a,b):
        sum=a+b
        print(sum)

    def sub(self,a,b):
        sub=a-b
        print(sub)

    def mult(self,a,b):
        mult=a*b
        print(mult)

    def division(self,a,b):
        division=a/b
        print(division)


object=Calc()
object.sum(5,6)
object.sub(6,5)
object.mult(5,2)
object.division(6,2)