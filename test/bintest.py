num = 123
aa = (num << 3) + (num << 1)

num_str = "91234578667"


class Number:
    base = ord('0')

    def __init__(self, text):
        self.value = self.parse(text)

    @classmethod
    def parse(cls, text):
        res = 0
        for value in text:
            res = (res << 3) + (res << 1)
            res += ord(value) - cls.base
        return res

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value


class DDD:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__["bb"] = "ggg"
        return instance


d = DDD("sss")
print(d.bb)


