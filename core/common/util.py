import os
import sys
import copy


class Util:
    @staticmethod
    def get_run_path():
        return os.path.split(os.path.realpath(sys.argv[0]))[0]

    @staticmethod
    def get_cwd():
        return os.getcwd()

    @staticmethod
    def get_config_path(filename):
        return os.path.join(Util.get_run_path(), "config", filename)

    @staticmethod
    def get_namespace(obj: object):
        return "{}.{}".format(obj.__module__, obj.__class__.__name__)

    @staticmethod
    def deepcopy(obj):
        return copy.deepcopy(obj)


