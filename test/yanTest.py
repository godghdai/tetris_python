class TestMetaClass(type):
    @staticmethod
    def log(fun):
        def inner(self, *args, **kwargs):
            print("start")
            fun(self, *args, **kwargs)
            print("end")

        return inner

    def __init__(cls, cls_name, bases, attr_dict):
        pass

    def __new__(cls, cls_name, bases, attr_dict):
        uppercase_attr = {"kkkk": "99999"}
        for name, val in attr_dict.items():
            if name.startswith('__'):
                uppercase_attr[name] = val
            else:
                if hasattr(val, "__call__"):
                    uppercase_attr[name] = cls.log(val)
                else:
                    uppercase_attr[name] = val

            if hasattr(val, "__call__"):
                print(val.__code__.co_varnames)
        return super().__new__(cls, cls_name, bases, uppercase_attr)


class Hello(dict, metaclass=TestMetaClass):
    data = 'abc'

    def __init__(self, name):
        super().__init__()
        self.name = name

    def word(self, text):
        print(self.name + ":" + text)


ss = Hello("sdfdsfds")
ss.word("123")
print(ss.kkkk)
print(ss.data)
