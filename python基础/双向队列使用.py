# -*- coding: utf-8 -*-
"""
====================================
@File Name ：双向队列使用.py
@Time ： 2022/10/27 10:16
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：了解队列的申明和常规的使用方法
====================================
"""
from collections import deque

# 双向队列的初始化
from random import randint

q = deque()
q1 = deque(randint(0, 100) for _ in range(100))
q2 = deque('123456')
print(q)
print(q1)
print(q2)

# 添加元素
print("============从队头添加元素=================")
q.appendleft('队首')
print("============从队尾添加元素=================")
q.append("队尾")
print(q)
print("=============限制长度的deque添加元素=========================")
q4 = deque([1, 2, 3, 4, 5, 6], maxlen=5)
# 当长度超过限制的长度，会从队首剔除元素
print(q4)
print("指定位置添加元素")
q2.insert(2, 7)
print(q2)

# 删除元素
print("从队首弹出元素")
q2.popleft()
print("从队尾弹出元素")
q2.pop()
print("删除指定元素")
# q2.remove(3)


# 添加序列
print("队首添加序列")
q1.extendleft(["队首添加序列", 1])
print("队尾添加序列")
q1.extend(['队尾添加序列', 1])

# 旋转
# num -- 从序列的第num个位置整体旋转
# 若num>=1，表示从右向左的num个数，与其左边的所有数顺时针旋转
# 若num<=-1，表示从左向右的-num个数，与其右边的所有数逆时针旋转

q6 = deque(num for num in range(10))
print(q6)
q6.rotate(3)
print(q6)

q7 = deque(num for num in range(10))
print(q7)
q7.rotate(-3)
print(q7)
