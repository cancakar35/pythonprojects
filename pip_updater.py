#!/usr/bin/env python
# -*- coding: utf-8 -*-

# github.com/cancakar35

import os

os.system("pip freeze > pip_packages.txt")

with open ("pip_packages.txt", "r", encoding="utf-8") as pkg_file:
    for i in pkg_file.readlines():
        i = i[:i.index("=")]
        cmnd = "pip install {} --upgrade".format(i)
        os.system(cmnd)

os.remove("pip_packages.txt")
print("All packages updated!")
