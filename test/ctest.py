def test():
    a = "b"
    b = "b"
    print(id(a))
    print(id(b))
    print(a == b)


def fun(**kwargs):
    print(kwargs)


def printf(**kwargs):
    format_str = ["'key:{key}'".format(key=key) for key in kwargs.keys()]
    print(",".join(format_str))
    # print(",".join(format_str), kwargs)


# parm = {"key": "key2", "value": "value2"}
# fun(key="key1", value="value1")
# fun(**parm)
# printf(key="food", value="1")


from typing import Union
import string

import re


class Number:
    reg_num = re.compile('^[0-9]*$')

    def __init__(self, value):
        self.value = Number.parse(value)

    @staticmethod
    def parse(value):
        if hasattr(value, "__int__"):
            return int(value)
        if hasattr(value, "__float__"):
            return float(value)

        if hasattr(value, "__str__") \
                and Number.reg_num.match(str(value)):
            return int(str(value))

        raise Exception("{} Not a Number".format(value))

    def __int__(self):
        return self.value


def sum2(*args):
    print(type(args))
    res = 0
    for num in args:
        res += Number.parse(num)
    return res


num1 = Number(1)
num2 = Number(2)
print(sum2(num1, num2, '55', 4.0))

print(sum((1, 2)))


def abc(a, b, *args, **kwargs):
    c, d = args
    print(f"a={a},b={b},c={c},d={d}")
    print(type(kwargs))


# abc(1, 2, 3, 4, e=5, f=6)


a, *b, c = {'a': 1, 'b': 2, 'cd': 3, 'ef': 4}
print(b)

for i in range(1, 5):
    for j in range(2, 7):
        print(i, j)
        if j == 5:
            print("--------------")
            break
    else:
        continue


def is_even(num):
    return not (num & 1)

print(is_even(-40))