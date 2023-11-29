# num=int(input("enter any number"))
# n=str(num)
# if len(n)==1:
#     print("one digit num")
# elif len(n)==2:
#     print("two digit num")
# elif len(n)==3:
#     print("three digit num")
# else:
#     print("more than three digit")

# char=input("enter anything")
# if 'A'<=char<='Z'or'a'<=char<='z':
#     print("it is alphabates")
# elif '0'<=char<='9':
#     print("it is number")
# else:
#     print("it is special character")

# char=input("enter any word")
#
# if char in "aeiou":
#     print ("vowel")
# else:
#     print("consonant")

# har = input("enter any word")
# if char[-1] in "aeiouAEIOU":
#     print("vowel")
# else:
#     print("consonant")

# char=input("enter any word")
# if char in('aeiou'):
#     print('vowel')
# else:
#     print("iconsonant")
# count=1
# while count <=100:
#     n=str(count)
#     if n[0]=='7' or n[-1]=='7':
#         print(count)
#     count+=1

# count = 1
# while count <= 100:
#      n = str(count)
#      if n[0] == '2' and n[-1] == '3' or n[0]=='3' and n[-1]=='2':
#          print(count)
#      count += 1
#
# count = 1
# while count <= 1000:
#      n = str(count)
#      if n[0] == '2' and n[-1] == '2' and n[1]=='2':
#          print(count)
#      count+=1

# s="hello world"
# index=0
# while index < len(s):
#     if index%2==0:
#         print(s[index])
#     index+=1
#
# s="hello world"
# index=0
# while index < len(s):
#     if index%2==1:
#         print(s[index])
#     index+=1
#
# l=[]
# count=1
# while count <=10:
#     l.append(count)
#     count+=1
# print(l)

# wap to count the numer of alphabate in the above sting using while not loop

# s="jalaj420@gmail.com"
# index=0
# alp=0
# while index <len(s):
#     char=s[index]
#     if'a'<= char <='z':
#         print(char)
#         alp=alp+1
#     index+=1
# print(alp)

# s="jalaj420@gmail.com"
# index=0
# alp=0
# while index <len(s):
#     char=s[index]
#     if'a'<= char <='z' or '0'<=char<='9':
#         print(char)
#         alp=alp+1
#     index+=1
# print(alp)


# s="jalaj420@gmail.com"
# index=0
# alp=0
# while index<len(s):
#     char=s[index]
#     if 'a'<= char<= 'z' or '0' <= char<= '9':
#         alp=alp+1
#     index+=1
# n=len(s)-alp
# print('the special characte+',n)

# l=[1,2,3,4,5,6]
# index=0
# while index <len(l):
#     print(l[index])
#     index+=1

# l=[10,20,30,40]
# sum=0
# for x in l:
#     sum=sum+x
# print(sum)

# s="hello world"
# for x in s:
#     print(x)

# s="hello world"
# for x in range (5):
#     print(x,s)


# l=[10,20,30,40]
# sum=0
# index=0
# for x in l:
#     sum=sum+x
#     if index%2==0:
#       index+=1
# print(x)

# s="ajaysAwle"
# l=[]
# for char in s:
#     if char in 'aeiouAEIOU':
#         l.append(char)
# print(l)

# s="ajaysAwle"
# l=[]
# k=[]
# for char in s:
#     if char in 'aeiouAEIOU':
#         l.append(char)
#     else:
#         k.append(char)
# print(k)


# d={}
# for ascii in range (ord('a'),ord('z')+1):
#     char=chr(ascii)
#     d[char]=ascii
# print(d)

# d={}
# for ascii in range (chr(97),chr(120)):
#     char=ord(ascii)
#     d[char]=ascii
# print(d)

# for x in range(65,91):
#     print(chr(x),x)

# d={}
# for ascii in range (ord('A'),ord('z')+1):
#     char=chr(ascii)
#     d[char]=ascii
# for x in d:
#     var=d[x]
#     if x in "AEIOUaeiou":
#         print(x,var)

# d={}
# for ascii in range (ord('A'),ord('z')+1):
#     char=chr(ascii)
#     d[char]=ascii
# for x in d:
#     var=str(d[x])
#     if var [0]=='5' or var [-1]=='7' or var[0]=='7' or var [-1]=='5':
#      print(x,var)

# d={}
# for ascii in range (ord('A'),ord('z')+1):
#     char=chr(ascii)
#     d[char]=ascii
# for x in d:
#     var=str(d[x])
#     if var [-1]=='2' or var [-1]=='4' or var[-1]=='6' or var [-1]=='8' or var [-1]=='0':
#      print(x,var)
# import random
# a=int(input("enter any number between 1 to 9"))
# b=random.randrange(1,10)
# print(b)
# if a>b:
#     print("number is bigger than guess")
# elif b>a:
#     print("number is smaller than guess")
# else:
#     print("both are equal")

#break and continue####
#break
# for a in range(1,10):
#     if a%2==0:
#         break
#     print(a)

#continue

# for a in range(1,10):
#     if a%3==0:
#         continue
#     print(a)

# a=b=c="ajay",22,99.99
# print(a)
#
# num=int(input("ent any numbr"))
# if (num%2==0):
#       print("even")
# else:
#     print("not even")

count=4
while(count>=1):
    print(count)
    count-=1