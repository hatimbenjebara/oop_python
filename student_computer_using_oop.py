#first things we need to know if you want an objet you need a class
#structure like integer float is build types 
class computer :
    #attributes is variables 
    #behaviour is methods or functions 
    #we will use a special methodes and theres two 
    #special variables which is _name_ 
    #special methods which is _init_
    def __init__(self): #to initialise variable
        print("in init") #for automatique, for each object it's do it one time 
    def config(self): #method
        print("this is high figure machine i5 1T")        
a = 5 # a is variable 
b = computer() # b is an object
print(type(b)) # <class '__main__.computer'> that's type mean this is a class this below to computer 
computer.config(b) #
b2 =computer()
b2.config() # it's same as computer.config(b) and this is senteces must used 
class name :   
    def __init__(self, first_name, last_name, age): #to accepte variable we need to add two variable in initial
        self.first_name= first_name # variables of each object
        self.last_name = last_name
        self.age = age
    def compare (self,other):
        if self.age == other.age:
            return True
        else:
            return False
    def call(self): #method variable
        print("hello ",self.first_name, " ", self.last_name, "have a ", self.age,"years olds")
a=name('hatim','benjebara', 35) # here variable first_name = hatim and last_name = benjebara    
a.call() 
b = name('fah', 'fahfah', 30)
b.call()
if a.compare(b): 
    print("they are at the same age")
else:
    print("they are at different age")
b.first_name='sweet'# change a local variable 
b.age=35
b.call()
#variable there are two type : instance variable and class(static) variable 
#namespace is an area where you create and store object/variable
#methods we have 3 : instance methods, class methods and static methods
class student:
    school='fst'# static variable come from out side the class
    student=1 #class variable below to class name space
    def _init_(self, m1,m2,m3): #instance methode know it by (self), 
        self.m1=m1 #instance variables inside int and there's 3 instances variables below to instance namespace
        self.m2=m2 
        self.m3=m3 
    def avg(self): #instance methode because of self its mean that something below to the instance 
        return (self.m1+self.m2+self.m3)/3
    #instance methods existe two different methods : first accessor methods and seconde mutator methods
    def get_m1(self):# getters methods is acccesor methods and we must create 3 for 3 variable 
        return self.m1
    def get_m2(self): 
        return self.m2
    def get_m3(self): 
        return self.m3
    def set_m1(self, value):#setters methode is mutator methods 
        self.m1=value
    def set_m2(self, value): 
        self.m2=value
    def set_m3(self, value):
        self.m3=value
    #create class methods
    @classmethod #decoretor
    def getschool(cls): # we know it it class methods by cls
        return cls.school
    #static method depend de class and instance
    @staticmethod
    def info():
        print("this is student class in latine")
s1=student()
s2=student()
s1.set_m1(16)
s1.set_m2(18)
s1.set_m3(20)
print(s1.avg())
print(student.getschool())
print(student.info())
