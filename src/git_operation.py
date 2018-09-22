#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import git
import os
from git import Repo

class GitConfig(object):
    def __init__(self):
        super(GitConfig, self).__init__()
        self.project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/')
        self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_list')
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/'))

    def install_project(self, url):
        try:
            git.Git(self.project_path).clone(str(url))
            print("successful git clone plugin")
        except Exception as e:
            print(e)

    def create_tag(self, plugin_name, version):
        try:
            obj = Repo(self.plugin_path.format(plugin_name))
            obj.create_tag("v"+str(version))
            print("successful create tag")

            # obj.remote.origin.push("tagname")
        except Exception as e:
            print(e)

    def create_branch(self, plugin_name, version):
        try:
            obj = Repo(self.plugin_path.format(plugin_name))
            new_branch = obj.create_head("v"+str(version)+"-branch")
            new_branch.checkout()  # bu satırda oluşturulan yeni branch e geçiyor. Yapılan değişiklikler yeni branch üzeinden yapılacak.
            print("successful create branch in local server")
        except Exception as e:
            print(e)