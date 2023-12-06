# #EXCEPTION HANDLIN
#
# a=5
# b=0
# try:
#     c=5/0
#     print(c)
# except:
#     print("plz enter a right digit")
#
#
# try:
#     age=int(input("enter your age"))
#     print(age)
# except:
#     print("enter a numeric value")

# a=10
# b=0
# try:
#     c=a/b
#     print(c)
# except Exception as e:
#     print("plz enter right num",e)


# a=4
# b=2
# try:
#     c=a/b
#     print('c',c)
# except ZeroDivisionError:
#     print("check your division is zero")
# else:
#     print("your division is greater than zero")

#01/12/2023

# a=10
# b=0
# try:
#     c=a/b
#     print('c:',c)
# except ZeroDivisionError as e:
#     print("check your division is zero",e)
# finally:
#     print("always executed")

#Raise an excetion
# try:
#     number=int(input("enter your number"))
#     if number>10:
#         raise Exception('invalid number')
# except Exception as e:
#     print(e)


# try:
#     num1=int(input("enter a numerator"))
#     num2=int(input("enter a denominator"))
#     result=num1/num2
#
#     if result %1 !=0:
#         raise ValueError("result is not an integer")
#
#     if result<0:
#         raise  ValueError("result is negative")
#     print(f"the result of the division is:{result}")
#
# except ValueError as ve:
#     print(f"error:{ve}")
# except ZeroDivisionError:
#     print("error cannot divide ny zero")
# except Exception as e:
#     print(e)


class A:
    "i am python developer"
    name="rays"
    age=23
    print(name)

    def show(self):
        "i am a ajay"
        self.salary=1000
        print(self.salary)

obj=A()
print(A.age)
print(obj.__doc__)
obj.show()
print(obj.show.__doc__)