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
    final_res=get_filled_res(base_res, num)

    # step3. adjust
    random.shuffle(base_res)

    # remove consequent duplicate
    final_res = get_consequent_dedup_res(final_res, base_res)

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

# 一年级；上；人教版 1~5的认识和加减法；5以内的加法
def gen_grade1_a_renjiao_1to5_addition(num):
    # step1. display all
    base_res = []
    for i in range(1, 5, 1):
        for j in range(1, 5, 1):
            if i + j <= 5:
                problem_str = f"{i}+{j}=_"
                ans_str = f"{i}+{j}={i+j}"
                base_res.append((problem_str, ans_str))

    # step2. fill
    final_res = get_filled_res(base_res, num)

    # step3. adjsut
    random.shuffle(base_res)
    final_res = get_consequent_dedup_res(final_res, base_res)

    return final_res

######################################

# key to problem func mapping
KeyProblemTypeMapping = {
    'grade1_a_renjiao_chapter1_section1': gen_grade1_a_renjiao_1to5_compare,
    'grade1_a_renjiao_chapter1_section2': gen_grade1_a_renjiao_1to5_addition
}



