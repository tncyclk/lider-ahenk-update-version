#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import git_operation
import os
from git_operation import Repo

class Util(object):
    def __init__(self):
        super(Util, self).__init__()

    @staticmethod
    def replace_all(text, dic):
        try:
            for i, j in dic.items():
                text = text.replace(i, j)
            print("version güncellendi.")
            return text
        except Exception as e:
            print("version güncellendi." + str(e))

    @staticmethod
    def replace(file_name, old_data, new_data):
        with open(file_name, 'r') as file:
            filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(old_data, new_data)

        # Write the file out again
        with open(file_name, 'w') as file:
            file.write(filedata)

    @staticmethod
    def copy_package(self):
        pass