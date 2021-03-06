#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/27 11:47 上午
# @Author  : JieZhang
# @Email  : jiezhang@sogou-inc.com
# @File    : UnitTest.py
# @Description: 测试数学题目生成的结果

from MathProblemGenerator import *

if __name__ == '__main__':
    problem_nums = [10, 50, 100, 500, 1000]
    problem_key = 'grade1_a_renjiao_chapter1_section5'
    func = KeyProblemTypeMapping[problem_key]
    for num in problem_nums:
        print(f"===TEST NUM: {num}, FUNC NAME: {func.__name__}====")
        start_time = time.time()
        ans = func(num)
        end_time = time.time()
        print(ans)
        cost_ms = (end_time - start_time) * 1000
        print(f"===COST: {cost_ms} ms===================\n")
