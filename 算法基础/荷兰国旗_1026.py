# -*- coding: utf-8 -*-
"""
====================================
@File Name ：荷兰国旗_1026.py
@Time ： 2022/10/26 9:58
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：Partition 的过程：
给定一个数组 arr ，和一个整数 num 。把小于等于 num 的数放在数组的左边，大于 num 的数放在数组的右边 。
比如数组 int[] arr = {18, 15, 13, 17, 6, 20, 15, 9};
给定一个数 15 ，小于等于 15 的数放在数组的左边，大于 15 的数放在数组的右边。
分析 Partition 的过程：
分支1 ：arr[i] <= 15，arr[i]和 小于等于区 的右边一个元素交换，同时 小于等于区向右扩展1个 ，i++
分支2 ：arr[i] > 15，不做操作，只是 i++
初始化 i 、小于等于区：
i 初始值为0；
小于等于区右边界为 -1 。

链接：https://juejin.cn/post/7129310392328650759
====================================
"""
from random import randint


def dutch_flag(num, lis):
    # 初始化小于区和大于区
    let = -1
    more = len(lis)
    i = 0
    # 循环判断执行partition过程
    while i < more:
        # 分支1 ：arr[i] <= 15，arr[i]和 小于等于区 的右边一个元素交换，同时 小于等于区向右扩展1个 ，i++
        if lis[i] < num:
            lis[i], lis[let + 1] = lis[let + 1], lis[i]
            i += 1
            let += 1
        # 当前值等于比较值，i++
        elif lis[i] == num:
            i += 1
        # arr[i] > 15，arr[i]和 大于区的左边一个元素 交换，同时 大于区向左扩展1个 ，i不变（因为此时arr[i]还未和交换过来的数据进行比较）
        else:
            lis[more - 1], lis[i] = lis[i], lis[more - 1]
            more -= 1




if __name__ == '__main__':
    # 创建一个随机长度的随机list
    num = randint(20, 100)
    lis = [randint(0, 1000) for _ in range(num)]
    lis.append(num)
    dutch_flag(num, lis)
    print(num, lis)
