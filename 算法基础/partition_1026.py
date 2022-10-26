# -*- coding: utf-8 -*-
"""
====================================
@File Name ：partition_1026.py
@Time ： 2022/10/26 10:57
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe： 实现partition过程,即将数组中的数分成两个部分，大于num和小于等于num
====================================
"""
from random import randint


def partition(num, lis):
    index = 0
    small = -1
    length = len(lis)

    while index < length:
        # 当前数小于num,小于区的下一个数和当前数交换,i++
        if lis[index] <= num:
            lis[index], lis[small + 1] = lis[small + 1], lis[index]
            small += 1
        else:
            index += 1


if __name__ == '__main__':
    lis = [randint(0, 10000) for _ in range(randint(20, 50))]
    num = lis[-1]
    lis.append(num)
    partition(num, lis)
    print(num, lis)
