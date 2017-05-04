# -*- coding: utf-8 -*-
# 全局变量表

def _init(): # 初始化
    global _global_dict
    _global_dict = {}


def set_value(key,value):
    _global_dict[key] = value


def get_value(key,defValue=None):
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

