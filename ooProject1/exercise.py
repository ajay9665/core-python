##write a proram to find maximum of to numbers.

# a=int(input("1st num"))
# b=int(input("2nd num"))
# if a>b:
#     print(a,"is max")
# elif a==b:
#     print("both are eqaul")
# else:
#     print(b,"is max")


##write a proram to enerate 5 random number between 1 to 100.


# import random
# a=random.randint(1,100)
# b=random.randint(1,100)
# c=random.randint(1,100)
# d=random.randint(1,100)
# e=random.randint(1,100)
# print(a,b,c,d,e)


##write aprogram to find factorial of a given number....
#
# method--1
#
# import math
# a=int(input("enter no"))
# print(math.factorial(a))


#method 2

n=int(input("num"))
def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
        return result
print("factorial of",n,"is",factorial(n))