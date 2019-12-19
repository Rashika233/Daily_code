class parent:
    def __init__(self):
        self.string1='Hello'
        self.string2='people'
        
    
    def fun2(self):
        print("fun2 : ", self.String1) 
        return

class child(parent):
    def fun1(self):
        self.fun2()
        print("fun1 : ", self.string2)
        return

object1=parent()
object2=child()
object2.fun1()