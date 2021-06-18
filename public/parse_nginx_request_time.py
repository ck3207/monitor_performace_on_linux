# -*- coding: utf-8 -*-
# author： hspcadmin
# datetime： 2021/6/17 9:26 
# ide： PyCharm
import math

import matplotlib.pyplot as plt

class ParseNginxRequestTime:
    def __init__(self, filename):
        self.acess_log_filename = filename
        self.partition = {}    # {0: {"parition": [1, 10, 100, 1000], "data": []}}

    def get_request_time(self):
        """
        Sample of request_time :  "request_time": "0.011"
        :return: 
        """
        request_time_list = []
        with open(file=self.acess_log_filename, mode="r", encoding="utf-8") as f:
            while True:
                line = f.readline()
                if not line.strip():
                    break
                request_time = float(line.split(": ")[-1].replace('"', ''))
                request_time_list.append(request_time * 1000) # s --> ms
        return sorted(request_time_list)

    def add_partition(self, partition):
        """
        增加统计数据分区， 默认模式为： {0: {"parition": [1, 10, 100, 1000], "data": []}}
        partion 后的list是统计区间，上述结果会统计： time<1ms，1ms<=time<10ms, 100ms<=time<1000ms, time>1000ms
        :param partition: 
        :return: 
        """
        self.partition.setdefault(len(self.partition), partition)
        return self.partition

    def get_partition(self):
        return self.partition

    def fileter_partition_data(self, array, partitions):
        small, big = 0, 10000
        data_dic = {}
        for i, partition in enumerate(partitions):
            # partition = partition.get("partition")
            if i == 0:
                big = partition
            elif i < len(self.partition.values()):
                small, big = prefix, partition
            else:
                small, big = prefix, partition
            prefix = partition
            data_dic.setdefault("part-{0}_{1}".format(small, big), list(filter(lambda x: x >= small and x < big, array)))
        else:
            data_dic.setdefault("part->{0}".format(prefix),  list(filter(lambda x: x >= prefix, array)))
        return data_dic

    def quicksort(self, array):
        """快速排序(从大到小).
         快速排序程序执行时间：n*O(log n)"""
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            left = [i for i in array[1:] if i >= pivot]
            right = [i for i in array[1:] if i < pivot]
            return self.quicksort(left) + [pivot] + self.quicksort(right)

    def get_summary(self, data_dic):
        data_summary = {}
        for partition, data in data_dic.items():
            data_summary.setdefault(partition, len(data))
        return data_summary

    def _plot(self):
        pass


if __name__ == "__main__":
    parse_nginx_request_time = ParseNginxRequestTime(filename="../logs/a.log")
    request_time_list = parse_nginx_request_time.get_request_time()
    parse_nginx_request_time.add_partition(partition={"partition": [1, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 500, 1000], "data": []})
    partitions = parse_nginx_request_time.add_partition(partition={"partition": [10, 50, 100, 500, 1000], "data": []})

    subplots = 121
    tmp_index = 0
    plt.figure(figsize=(20, 8))
    for k, partition in partitions.items():
        partition_list = partition.get("partition")
        data_dic = parse_nginx_request_time.fileter_partition_data(request_time_list, partition_list)
        data_summary = parse_nginx_request_time.get_summary(data_dic=data_dic)

        x= [i for i in range(len(data_summary.keys()))]
        height = list(data_summary.values())
        tick_label = list(data_summary.keys())
        plt.subplot(subplots+tmp_index)
        plt.bar(x=x, height=height, tick_label=tick_label, fc="#87CEFA")

        fsum = math.fsum(height)
        for xx, yy in zip(x, height):
            plt.text(xx, yy, str(yy)+"\n{}%".format(round(yy/fsum * 100, 2)), ha='center')

        plt.xticks(rotation=-30)
        tmp_index += 1
    plt.show()