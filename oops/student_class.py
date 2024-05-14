

class Student:

    name:str
    rollno:int
    course:str

    def set_student(self,name,rollno,crse):
        self.name=name
        self.rollno=rollno
        self.course=crse

    def display_student(self):
        print(self.name,self.rollno,self.course)


st1=Student()
st1.set_student("radha",21,"python")

st2=Student()
st2.set_student("raju",57,"python")

st1.display_student()
st2.display_student()
