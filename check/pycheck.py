#!/usr/bin/env python3
'''library for validating the quality of python files'''
import ast
import os
import sys
import re
def has_py_syntax_errors(file_name):
    with open(file_name) as f:
        contents = f.read()
    try:
        ast.parse(contents)
        return False
    except SyntaxError:
        return True
def permissions_of(file_name):
    #664 is not chmoded 
    #775 is chmoded
    return int(oct(os.stat(file_name)[0])[-3:])
def file_to_list(file_name):

    with open(file_name) as f:
        lines = f.read().splitlines()
    return lines
def check_regex(expressions, content):
    has_missing = False
    missing = []
    for expression in expressions:
        regex = re.compile(expression)
        for line in content:
            if regex.match(line):
                break
        else:
            missing.append(expressions)

    if len(notWithin) != 0:
        has_missing = True
    return has_missing, missing

