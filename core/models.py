from dataclasses import dataclass

@dataclass
class BaseDAO:
    """Base DAO should handle set and get ie. set data to the database
       and get values from the database.
    """

    def save(self):
        self.process_meta_data()
        child_class: list = self.get_child_class()
        print(child_class)

    def get_child_class(self):
       print(self.__annotations__)

    def process_meta_data(self):
        meta_dict = None
        try:
            meta_dict = self.Meta.__dict__.items()
        except AttributeError:
            pass

        if meta_dict:
            user_vars = [(key, val) for key, val in meta_dict if not key.startswith('__')]
            print(user_vars)




# class CharField(object):
#     def __init__(self, max_length: int = None):
#         self.max_length = max_length
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.max_length]
#
#     def __set__(self, instance, value):
#         if len(value) > self.max_length:
#             raise Exception("MaxValException")
#         instance.__dict__[self.max_length] = value
#
#
# class TestObj:
#     my_name = CharField(min_length=2, max_length=4, null=True)
#
#
# t = TestObj()
# t.my_name = 'wsss'

#print(t.my_name)
##############################################################################################


# def positive_validator(name, value):
#     print(name, value)
#     if value <= 0:
#         raise ValueError(f"values for {name!r}  have to be positive")
#
#
# class MyAttr:
#     def __init__(self, type, maxsize=None, validators=()):
#
#         self.type = type
#         self.validators = validators
#         self.maxsize = maxsize
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         if not instance: return self
#         return instance.__dict__[self.name]
#
#     def __delete__(self, instance):
#         del instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, self.type):
#             raise TypeError(f"{self.name!r} values must be of type {self.type!r}")
#         for validator in self.validators:
#             validator(self.name, value)
#             instance.__dict__[self.name] = value
#
# #And now
#
# @dataclass
# class Person:
#     name: str = MyAttr(str)
#     age: float = MyAttr((int, float), 5, [positive_validator])
#
#
# p = Person('santhosh', -6)
# print(p.age)