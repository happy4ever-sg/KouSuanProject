#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 5:38 下午
# @Author  : JieZhang;ShiHang
# @Email  : jiezhang@sogou-inc.com;shihang@sogou-inc.com
# @File    : CommonUtils.py
# @Description: 常见子函数供调用

import random

# 比较类
def get_compare_sign(int_a, int_b):
    if int_a == int_b:
        return "="
    elif int_a > int_b:
        return ">"
    else:
        return "<"

def extract_compare_sign(compare_ans_str):
    if ">" in compare_ans_str:
        return ">"
    if "<" in compare_ans_str:
        return "<"
    return "="

# 填充函数
def get_random_filled_res(base_res, num):
    final_res=[]
    while len(final_res) < num:
        # shuffle
        random.shuffle(base_res)

        last_num = num - len(final_res)
        if last_num <= len(base_res):
            final_res.extend(base_res[:last_num])
        else:
            final_res.extend(base_res)
    return final_res

# 去除连续重复
def get_consequent_dedup_res(final_res, base_res):
    for idx in range(len(final_res)):
        if idx > 0 and final_res[idx][0] == final_res[idx-1][0]:
            for res in base_res:
                # random replace
                if res[0] != final_res[idx][0]:
                    final_res[idx] = res
    return final_res
