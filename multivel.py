class Base:
    def __init__(self,name):
        self.name=name

        def getName(self):
            return self.name
        class Child(Base):
            def __init__(self,name,age):
             Base.__init__(self,name)
             self.age=age
             def getAge(self):
                return self.age