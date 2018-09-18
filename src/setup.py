#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from util import Util
from git_operation import GitConfig
from update_lider_plugin import UpdateVersion



class VersionManager(object):
    def __init__(self):
        super(VersionManager, self).__init__()
        self.util = Util()
        self.git = GitConfig()
        self.update_version = UpdateVersion()

        self.project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/')
        self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_list')
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/'))

    def version_manager(self, plugin_name, version):
        with open(self.plugin_list_path, "r") as f:
            for url in f:
                print("---->>> plugin url: "+url)
                self.git.install_project(url)
                self.git.create_tag(plugin_name, version)
                self.git.create_branch(plugin_name, version)
                self.update_version.set_version(plugin_name, version)

if __name__ == '__main__':
    app = VersionManager()
    app.version_manager("script", "1.1.1.1")
