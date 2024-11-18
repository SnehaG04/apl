class A:
    def func1(self):
        print("This function is defined inside the parent class")


class B(A):
    def func2(self):
        print("This function is defined inside the child class.")
object=B()
object.func1()
object.func2()