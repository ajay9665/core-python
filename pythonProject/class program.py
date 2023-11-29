# #palindome (24/11/2023)
#
# string=input("enter a string")
# s=string.lower().replace("","")
# if s==s[::-1]:
#     print("the string is a palindrome")
# else:
#     print("the string is not a palindrom")

#prime number####

# number=int(input("enter a number"))
# if number>1:
#     for i in range(2,int(number**0.5)+1):
#         if number % i==0:
#             print("is not a prime number")
#             break
#     else:
#             print("its prime number")
# else:
#      print("it is not prime number")

# number=int(input("enter a number"))
# if number>1:
#     for i in range(2,number):
#         if number % i==0:
#             print("is not a prime number")
#             break
#     else:
#             print("its prime number")
# else:
#      print("it is not prime number")


#prime number (25/11/2023)

# number=int(input("enter a number"))
# if number>1:
#     for i in range(2,number):
#         if number % i==0:
#             print("is not a prime number")
#             print(i,"time",number//i,"and",number)
#             break
#     else:
#             print("its prime number")
# else:
#      print("it is not prime number")


#prime number in range
#
# a=int(input("enter any number"))
# b=int(input("enter any number"))
# for number in range(a,b):
#  if number>1:
#     for i in range(2,number):
#         if number % i==0:
#             break
#     else:
#             print(number,"its prime number")
# else:
#      print(number,"it is not prime number")