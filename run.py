# -*- coding: utf-8 -*-
# author： hspcadmin
# datetime： 2021/5/15 11:46 
# ide： PyCharm
from abc import ABCMeta

class PerformanceIndex(metaclass=ABCMeta):
    """定义性能指标方法"""
    def get_use_percentage(self):
        """获取使用率"""
        pass

    def draw(self):
        """数据指标描绘成图"""
        pass

class CPU:
    """监控CPU指标"""
    pass


class Sar:
    """Linux Sar 命令得文件解析"""
    pass

with open(file="a", mode="r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line)