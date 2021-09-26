#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/9/26 5:38 下午
# @Author  : JieZhang;ShiHang
# @Email  : jiezhang@sogou-inc.com;shihang@sogou-inc.com
# @File    : CommonUtils.py
# @Description: 常见子函数供调用


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

