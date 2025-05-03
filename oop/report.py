class A:
    def show(self):
        print("1")

class B(A):
    def show(self):
        print("2")
        super().show()

class C(A):
    def show(self):
        print("3")
        super().show()

class D(B, C):
    def show(self):
        print("4")
        super().show()

obj = D()
obj.show()
print(D.mro())  #--------> this is the sequence 



"""
1-Python uses Method Resolution Order (MRO) to decide which method to call.
2-The MRO ensures that each class in the hierarchy is called only once, and in a consistent order.
3-super() moves forward in the MRO list, not just to the immediate parent.
4-It prevents duplicate calls and supports cooperative multiple inheritance.
"""




class Human:
    def eat(self):
        print("Human eats")

class Mammal:
    def eat(self):
        print("Mammal eats")

class Employee(Human , Mammal):
    pass

e = Employee()
e.eat()

# notice if we revese the order of human and mammal 
class Human:
    def eat(self):
        print("Human eats")

class Mammal:
    def eat(self):
        print("Mammal eats")

class Employee(Mammal , Human):
    pass

e = Employee()
e.eat()
