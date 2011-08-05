import os
import re

class BroLogUtil(object):
    EXT_EXPR = re.compile(r"[^/].*?\.(.*)$")
    logtypes = dict()

    @staticmethod
    def supports(path):
        base, fname = os.path.split(path)
        return BroLogUtil.get_ext(fname) in BroLogUtil.logtypes

    @staticmethod
    def get_field_info(path):
        base, fname = os.path.split(path)
        return BroLogUtil.logtypes[ BroLogUtil.get_ext(fname) ]

    @staticmethod
    def register_type(file_ext, target):
        BroLogUtil.logtypes[file_ext] = target

    
    @staticmethod
    def get_ext(path):
        m = BroLogUtil.EXT_EXPR.search(path)
        if(m):
            return m.group(1)
        return None

