# -*- coding: utf-8 -*-
# author： hspcadmin
# datetime： 2021/5/23 19:50 
# ide： PyCharm
import random

class Generator:
    """造数据脚本
    条件单：用户id, stock_code, stock_name, exchange_type, 
    strategy_id = 
    """
    def __init__(self):
        self.sql_model = ""
        self.sql_num = 1

    def set_sql_model(self, sql_model):
        self.sql_model = sql_model

    def set_sql_num(self, sql_num):
        self.sql_num = sql_num

    def increase_id(self, start_id, length):
        target_list = []
        for i in range(length):
            target_list.append(start_id+i)
        return target_list

    @staticmethod
    def get_random_str(base_str, lenth):
        target_str = ""
        for i in range(lenth):
            target_str += random.choices(list(base_str))[0]
        return target_str



if __name__ == "__main__":
    # random.choices()
    generetor = Generator()
    random_str_list = []
    for i in range(1000):
        random_str_list.append(generetor.get_random_str(base_str="abcdefghijklmnopqrstuvwxyz1234567890", lenth=6))
    for each in random_str_list:
        print(each)

