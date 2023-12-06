### cuncurrency & treading

#hello wihout thread

# def hello():
#     for i in range(15):
#         print("hello",i)
#
# def hi():
#     for i in range(15):
#         print("hi",i)
# hello()
# hi()


##hello with thread

#
# import threading
# from threading import *
# def hello():
#     for i in range(15):
#         print("hello",i)
#
# def hi():
#     for i in range(15):
#         print("hi",i)
#
# t1=threading.Thread(target=hello)
# t2=threading.Thread(target=hi)
# t1.start()
# t2.start()


#
# import threading
# from threading import *
# def hello(name):
#     for i in range(15):
#         print(name,i)
#
# t1=threading.Thread(target=hello,args=('ram',))
# t2=threading.Thread(target=hello,args=('ajay',))
# t1.start()
# t2.start()

## Threadin with time methid

from time import sleep
from threading import Thread


class A(Thread):
    def run(self):
        for i in range(5):
            print("ajay bhaiya")
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(5):
            print("aman bhaiya")
            sleep(1)

t1=A()
t2=B()
t1.start()
t2.start()
t1.join()
t2.join()
print("jalaj")

### threadin with time

# from time import sleep
#
#
# class A:
#     def run(self):
#         for i in range(5):
#             print("ajay bhaiy")
#             sleep(1)
#
#
# class B:
#     def run(self):
#         for i in range(5):
#             print("aman bhaiya")
#             sleep(1)
#
# t1=A()
# t2=B()
# t1.run()
# t2.run()
