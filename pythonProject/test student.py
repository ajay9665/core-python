import  student

student.add_student(1,"jalaj")
student.update_student(2,"aman")

import student as st
st.add_student(3,"ajay")
st.update_student(1,"rays")

from student import add_student,update_student
add_student(5,"ajay")
update_student(6,"aman")

from student import *
add_student(7,"banti")
update_student(3,"vikas")

from student import  add_student as ast
ast(9,"ncs")
update_student(7,"ncs")