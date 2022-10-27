# -*- coding: utf-8 -*-
"""
====================================
@File Name ：和至少为K的最短数组_862_1026.py
@Time ： 2022/10/26 16:42
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：给你一个整数数组 nums 和一个整数 k ，找出 nums 中和至少为 k 的 最短非空子数组 ，并返回该子数组的长度。如果不存在这样的 子数组 ，返回 -1 。
子数组 是数组中 连续 的一部分。


结题思路
    利用单调队列获取最短的两个数
    知识要点 队列 前缀和
链接：https://leetcode.cn/problems/shortest-subarray-with-sum-at-least-k
====================================
"""
from collections import deque
from itertools import accumulate
from random import randint


def shortestSubarray(nums, k):
    # 实现前缀和
    preSumArr = [0]
    # 标记长度
    res = len(nums) + 1
    for num in nums:
        preSumArr.append(preSumArr[-1] + num)

    # 申明一个队列
    q = deque()

    # 循环遍历
    for i, curSum in enumerate(preSumArr):
        # 当q不为空
        # 当q 不为空,且当前数减去q首的元素，大于等于k
        while q and curSum - preSumArr[q[0]] >= k:
            res = min(res, i - q.popleft())
        #  当q 不为空，q的队末大于都等于当前前缀和
        while q and q[-1] >= curSum:
            q.pop()
        # 当q 为空
        q.append(i)
    return res if res < len(nums) + 1 else -1


if __name__ == '__main__':
    nums = [randint(0, 1000) - randint(0, 1000) for _ in range(100)]
    k = 40
    shortestSubarray(nums, k)
