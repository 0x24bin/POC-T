#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = i@cdxy.me
# project = https://github.com/Xyntax/POC-T

"""
测试用例
"""

import random
import time


def poc(str):
    time.sleep(3)
    if random.randint(1, 10) > 5:
        return True
    return False
