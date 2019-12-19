def fun1():
    print('hello outer fun1')
    def fun2():
        print('hello inner fun2')
    fun2()
