#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 5:38 下午
# @Author  : JieZhang;ShiHang
# @Email  : jiezhang@sogou-inc.com;shihang@sogou-inc.com
# @File    : MathProblemGenerator.py
# @Description: 小学一年级口算题目生成

import random
import time
from CommonUtils import *
from GlobalParams import *

# generate funcs, input: num(int), output: list<problem, answer>

# 一年级；上；人教版 1~5的认识和加减法；5以内的数比大小
def gen_grade1_a_renjiao_1to5_compare(num):
    # step1. display all
    base_res=[]
    for i in range(0, 5, 1):
        for j in range(0, 5, 1):
            problem_str = f"{i}_{j}"
            ans_str = f"{i}{get_compare_sign(i, j)}{j}"
            base_res.append((problem_str, ans_str))

    # step2. fill
    final_res=[]
    while len(final_res) < num:
        # shuffle
        random.shuffle(base_res)

        last_num = num - len(final_res)
        if last_num <= len(base_res):
            final_res.extend(base_res[:last_num])
        else:
            final_res.extend(base_res)

    # step3. adjust
    random.shuffle(base_res)

    # remove duplicate
    for idx in range(len(final_res)):
        if idx > 0 and final_res[idx][0] == final_res[idx-1][0]:
            for res in base_res:
                # random replace
                if res[0] != final_res[idx][0]:
                    final_res[idx] = res

    # remove consequent compare
    for idx in range(len(final_res)):
        if idx >= 2:
            sign1 = extract_compare_sign(final_res[idx-2][1])
            sign2 = extract_compare_sign(final_res[idx-1][1])
            sign3 = extract_compare_sign(final_res[idx][1])
            if sign1 == sign2 and sign2 == sign3:
                for res in base_res:
                    # random replace
                    replace_sign = extract_compare_sign(res[1])
                    if replace_sign != sign2:
                        final_res[idx] = res

    # random add
    if len(final_res) < num:
        add=base_res[:num-len(final_res)]
        random.shuffle(add)
        final_res.extend(add)

    return final_res

######################################

# key to problem func mapping
KeyProblemTypeMapping = {
    'grade1_a_renjiao_1to5_compare': gen_grade1_a_renjiao_1to5_compare
}

if __name__ == '__main__':
    #TEST
    problem_nums = [5, 10, 50, 100, 500, 1000]
    problem_key = 'grade1_a_renjiao_1to5_compare'
    func = KeyProblemTypeMapping[problem_key]
    for num in problem_nums:
        print(f"===TEST NUM: {num}====")
        start_time = time.time()
        ans = func(num)
        end_time = time.time()
        print(ans)
        cost_ms = (end_time - start_time) * 1000
        print(f"===COST: {cost_ms} ms===================\n")


