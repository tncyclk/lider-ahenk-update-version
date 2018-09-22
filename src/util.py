#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import shutil
import subprocess
import select


class Util(object):
    def __init__(self):
        super(Util, self).__init__()
        self.plugin_version_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_version.ods')

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
        try:
            with open(file_name, 'r') as file:
                filedata = file.read()

            # Replace the target string
            filedata = filedata.replace(old_data, new_data)

            # Write the file out again
            with open(file_name, 'w') as file:
                file.write(filedata)
        except Exception as e:
            print(e)

    @staticmethod
    def copy_file(source_full_path, destination_full_path):
        try:
            shutil.copy2(source_full_path, destination_full_path)
        except Exception as e:
            print(e)

    @staticmethod
    def move(source_full_path, destination_full_path):
        try:
            shutil.move(source_full_path, destination_full_path)
        except:
            raise

    @staticmethod
    def is_exist(full_path):
        try:
            return os.path.exists(full_path)
        except:
            raise

    @staticmethod
    def create_directory(dir_path):
        try:
            if os.path.exists(dir_path):
                print("dizin zaten var")
            else:
                return os.makedirs(dir_path)
        except:
            raise

    @staticmethod
    def execute_command(command, working_directory):

        try:
            process = subprocess.Popen(command, stdin=None, env=None, cwd=working_directory, stderr=subprocess.PIPE,
                                       stdout=subprocess.PIPE, shell=True)
            for line in iter(process.stdout.readline, b''):
                print(line)
            process.stdout.close()
            result_code = process.wait()

            p_out = process.stdout.read().decode("unicode_escape")
            print(p_out)
            p_err = process.stderr.read().decode("unicode_escape")
            if result_code == 0:
                print(str(command) + " komutu başarıyla çalıştırıldı")
            else:
                print(str(command) + " komutu çalıştırılırken hata oluştu! " + str(p_err))
        except Exception as e:
            print(e)

    @staticmethod
    def read_file(full_path, mode='r'):
        content = None
        try:
            with open(full_path, mode) as f:
                content = f.read()
        except:
            raise
        finally:
            return content

    @staticmethod
    def write_file(full_path, content, mode='a+'):
        file = None
        try:
            file = open(full_path, mode)
            file.write(content)
        except:
            raise
        finally:
            file.close()



