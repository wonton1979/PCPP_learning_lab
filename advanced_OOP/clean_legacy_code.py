import datetime
from time import sleep


def get_instantiation_time(self):
    return self.instantiation_time

class MyMetaClass(type):
    instantiated_name_list = list()
    def __new__(mcs, name, bases, attrs):
        attrs["instantiation_time"] = datetime.datetime.now()
        attrs["get_instantiation_time"] = get_instantiation_time
        obj = super().__new__(mcs, name, bases, attrs)
        MyMetaClass.instantiated_name_list.append(name)
        return obj

class MyClassOne(metaclass=MyMetaClass):
    def __init__(self):
        print("Hello")

sleep(3)

class MyClassTwo(metaclass=MyMetaClass):
    def __init__(self):
        print("World")


print(MyClassOne.__dict__)
test1 = MyClassOne()
print(test1.get_instantiation_time())

test2 = MyClassTwo()
print(test2.get_instantiation_time())
print(MyMetaClass.instantiated_name_list)