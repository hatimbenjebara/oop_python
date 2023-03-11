#inheritance 
class A:#A is superclass
    def feature1(self):
        print("freature 1 is working")
    def feature2(self):
        print("freature 2 is  working")
class B(A) : #inheritance using features of existing class and B subclass and we can multipal lie Class C(A,B)
    def feature3(self):
        print("freature 3 is working")
    def feature4(self):
        print("freature 4 is  working")
a1=A()
a1.feature1()
a1.feature2()
b1=B()
b1.feature1()
b1.feature2()
b1.feature3()
b1.feature4()
#constructor
class A:
    def _init_(self):
        print("in A unit")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working ")
class B(A):
    def _init_(self):
        super()._init_()# call init of A
        print("in B unit")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working ")
class D:
    def _init_(self):
        print("in A unit")
    def feature1(self):
        print("feature1-D is working")
    def feature2(self):
        print("feature2-D is working ")
class C(A,D):#method resolution order
    def _init_(self):
        super._init_() # from left to right
        print("in C init")
a1=B()
a1.feature1()
a1._init_()
c1=C()
c1.feature1()
#polymorphisme mean multiple forms 
#duck typing 
class visual_studio:
    def execute(self):
        print("compiling")
        print("running")
class laptoop: 
    def code(self, ide):
        ide.execute()# ide
ide=visual_studio()
lap1=laptoop()
lap1.code(ide)
 

