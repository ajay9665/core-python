from  shape import Shape

s=Shape("green",2)
s.setColor(input("enter color"))
print(s.getColor())
s.setBorderWidth(3)
print(s.getBorderWidth())

print(Shape.PI)
print(s.getPi())

from Rectangle import Rectangle

obj=Rectangle("red",12,2,3)
print(obj.getLength())
print(obj.getColor())
print(obj.getBorderWidth())
print(obj.getWidth())

from Circle import Circle
cir=Circle("red",6)
cir.setRadius(12)
print(cir.getPi())
print(cir.area())

