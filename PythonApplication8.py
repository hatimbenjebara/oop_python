#operator overloading
a=3
b=2
print(int.__add__(a,b)) # this is a same as print(a+b)
class student:
    def __init__(self,m1,m2):
        self.m1=m1 
        self.m2=m2 
    def _add_(self,other):
        m1=self.m1 + other.m1 
        m2=self.m2 + other.m2
        s3=student(m1,m2)
        return s3
    def _gt_(self,other):
        r1=self.m1+self.m2
        r2=self.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
    def _str_(self):
        return self.m1, self.m2
s1=student(18,20)
s2=student(17,20) 
s3=student._add_(s1,s2) # here we cant use s3 = s1+s2 this not working
print(s3.m1)
s4=student._gt_(s1,s2) # here we cant use s1<s2
if s4== True :
    print("s1 wins")
else:
    print("s2 wins")
print(s1._str_()) # now we can affiche a s1 not a adress 
#revision 
class item:
    pay_rate=0.8 #the pay rate agter 20% discount
    def __init__(self, name: str, price : int, quantity=0): #name : to precize a type of name 
        #run validation to the received arguments
        assert price >=0, f"price {price} is not greater than zero!"
        assert quantity >=0, f"quantity {quantity} is not greater or equal to zero" 
        self.name=name 
        self.price=price 
        self.quantity=quantity 
        #actions to execute
        #item.all.append(self)

    def calculate_total_price(self):
        return self.price*self.quantity 
    def apply_discount(self):
        self.price=self.price*item.pay_rate
item1=item('iphone_13_pro_max',900,2)
item2=item('samsung_S_22',1100,5)

print(item1.calculate_total_price()) 
print(item2.calculate_total_price())
