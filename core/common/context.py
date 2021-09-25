from .util import Util


class Context:
    singleton = None

    def __init__(self):
        self.__dic = {}

    @classmethod
    def get_instance(cls):
        if not cls.singleton:
            cls.singleton = cls()
        return cls.singleton

    def register(self, obj: object):
        key = Util.get_namespace(obj)
        if key in self.__dic:
            raise Exception("context register error")
        print("{} register in context".format(key))
        self.__dic[key] = obj

    def unregister(self, obj: object):
        key = Util.get_namespace(obj)
        if key not in self.__dic:
            raise Exception("context unregister error")
        # print("{} unregister in context".format(key))
        del self.__dic[key]

    def get(self, classpath: str):
        key = classpath
        if key not in self.__dic:
            raise Exception("get error")
        return self.__dic[key]

    @staticmethod
    def module_register(obj: object):
        return Context.get_instance().register(obj)

    @staticmethod
    def module_unregister(obj: object):
        return Context.get_instance().unregister(obj)

    @staticmethod
    def get_module(classpath: str):
        return Context.get_instance().get(classpath)

    @staticmethod
    def get_config():
        return Context.get_module("core.common.config.Config")

    def __str__(self):
        return ",".join(self.__dic.keys())
