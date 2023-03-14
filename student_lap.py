#we can have a class inside a class 
class student:
    def _init_(self,name,rollno):
        self.name=name 
        self.rollno= rollno
        self.lap=self.laptop()
    def show(self):
        print(self.name, self.rollno)
        self.laptop.show(self) #missing something 
    def get_name(self): 
        return self.name
    def get_rollno(self): 
        return self.rollno
    def set_name(self, value): 
        self.name=value
    def set_rollno(self, value):
        self.rollno=value
    class laptop: #class inside class when you pass lot of variable we call class inside better then method
        def _init_(self):
            self.brand='HP'
            self.cpu='i5'
            self.ram= 8
s1=student()
s1.set_name('hatim benjebara')
s1.set_rollno(3)
lap1=student.laptop()
print(lap1)
