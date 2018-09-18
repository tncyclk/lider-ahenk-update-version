#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import git
import os
from git import Repo

class UpdateVersion(object):
    def __init__(self):
        super(UpdateVersion, self).__init__()
        self.project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins/')
        self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugin_list')
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins/lider-ahenk-{}-plugin')


        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plugins/'))

    def replace_all(self, text, dic):
        try:
            for i, j in dic.items():
                text = text.replace(i, j)
            print("version güncellendi.")
            return text
        except Exception as e:
            print("version güncellendi." + str(e))


    def install_project(self):
        try:
            with open(self.plugin_list_path, "r") as f:
                for line in f:
                    print(line)
                    git.Git(self.project_path).clone(str(line))
                    print("successful git clone plugin")
        except Exception as e:
            print(e)

    def create_tag(self):
        obj = Repo(self.plugin_path.format("script"))
        obj.create_tag("v1.2")

        # obj.remote.origin.push("tagname")

    def create_branch(self):
        obj = Repo(self.plugin_path.format("script"))
        new_branch = obj.create_head("v1.2-branch")
        new_branch.checkout()  # bu satırda oluşturulan yeni branch e geçiyor. Yapılan değişiklikler yeni branch üzeinden yapılacak.

    def set_version(self):
        pass

    def copy_packages(self):
        pass




if __name__ == '__main__':
    app = UpdateVersion()
    # app.install_project()
    # app.create_tag()
    app.create_branch()