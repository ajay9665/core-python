# from  shape import Shape
#
# s=Shape("green",2)
# s.setColor(input("enter color"))
# print(s.getColor())
# s.setBorderWidth(3)
# print(s.getBorderWidth())
#
# print(Shape.PI)
# print(s.getPi())
#
# from Rectangle import Rectangle
#
# obj=Rectangle("red",12,2,3)
# print(obj.getLength())
# print(obj.getColor())
# print(obj.getBorderWidth())
# print(obj.getWidth())
#
# from Circle import Circle
# cir=Circle("red",6)
# cir.setRadius(12)
# print(cir.getPi())
# print(cir.area())

# from triangle import triangle
# tra=triangle(12,34,12)
# print(tra.area())
# para=triangle(12,34,12)
# print(para.parameter())

from triangle import  triangle
s=triangle(0,0,0)
s.setlength(int(input("num")))
s.setbase(int(input("num")))
s.setthirdside(int(input("num")))
print(s.area())