#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

DATABASE = {
    # 'name':'student',
    'path': "%s\db\database" % BASE_DIR
}

