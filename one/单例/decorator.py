

def SingleTon(cls,*args, **kwargs):
    instances = {}
    def _sigleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _sigleton

@SingleTon
class TestClass(object):
    a = 1

test1 = TestClass()
test2 = TestClass()
print(test1.a,test2.a)

test1.a = 2
print(test1.a,test2.a)

print(id(test1),id(test2))