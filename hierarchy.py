class Parent1:
    def func1(self):
        print("This function is defined inside the parent class")



class Child1(Parent1):
    def func2(self):
        print("This function is defined inside the child 1.")

class Child2(Parent1):
    def func2(self):
        print("This function is defined inside the child 2.")

object1=Child1()
object2=Child2()
object1.func1()
object1.func2()                      
object2.func1()
object2.func3()