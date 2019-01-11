# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:33:20 2018

@author: Li Zeng hai
"""
#python build_pyd.py build_ext --inplace

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='any words.....',
    ext_modules=cythonize(['Start.py','UI/UiController.py','UI/UI.py','Widget/LineEdits.py',]),
)