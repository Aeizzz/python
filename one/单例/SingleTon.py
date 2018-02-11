

class SingleTon(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = object.__new__(cls,*args, **kwargs)
        return cls._instance

class TestClass(SingleTon):
    a = 1

test = TestClass()
test2 = TestClass()
print(test.a,test2.a)

test.a = 2
print(test.a,test2.a)

print(id(test),id(test2))