#!/usr/bin/env python
#! -*- coding:utf-8 -*-
import os

def get_current_path():
    current_path = os.path.abspath(__file__)
    return(os.path.abspath(os.path.dirname(current_path) + os.path.sep + "."))
