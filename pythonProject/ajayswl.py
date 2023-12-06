# file=open("ajay.txt",'r')
# content=file.read()
# file.close()
# print(file.mode)
# print(file.closed)
# print(content)

# with open("ajay.txt",'r') as file:
#     content=file.read()
#     print(content)
#     print(file.mode)
#     file.close()
# print(file.closed)

# file=open("ajay.txt",'w')
# file.write("i am good")
# print("data write succesfully")
#
# file=open("ajay.txt",'r')
# content=file.read()
# print(content)

# file=open("ajay.txt",'r')
# content=file.read()
# file.close()
# print(file.mode)
# print(content)
# file=open("ajay.txt",'w')
# file.write("i am good")
# print("data write succesfully")

# file=open("ajay.txt",'r')
# content=file.read()
# print(content)
#
# file=open("ajay.txt",'rw'O)
# print("file.name")
# print(file.mode)
# print(file.closed)
# file.close()
#

#04/12/2023


# file=open("ajay.txt")
# for line in file:
#     print(line)
# file.close()

# file=open("ajay.txt",'w')
# file.write("hi\n")
# file.write("i am ajay\n")
# file.write("bhai aman")
# file.close()

#
# with open("ajay.txt",'w') as file:
#     file.write("hi\n")
#     file.write("am ajay")

# file=open("ajay.txt")
# for line in file:
#     print(line)
# file.close()
# file=open("ajay.txt",'r')
# str=file.read(5)
# print(str)
# position=file.tell()
# print(position)


# import os
# # os.rename("ajay.txt","aman.txt")
# os.rename("aman.txt","ajay.txt")

# import pickle
# l=[1,2,3,4,5,6]
# file=open("ajay.txt",'wb')
# pickle.dump(l,file)
# file.close()

# import pickle
# file=open("ajay.txt",'rb')
# l=pickle.load(file)
# print(l)
