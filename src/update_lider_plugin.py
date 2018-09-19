#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from util import Util
from git_operation import GitConfig
class UpdateVersion(object):
    def __init__(self):
        super(UpdateVersion, self).__init__()
        self.util = Util()
        self.git = GitConfig()


        self.project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/')
        self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_list')
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')


        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/'))

    def set_version(self, plugin_name, version):
        print(version)
        file_1 = self.plugin_path.format(plugin_name)+"/pom.xml"
        print("----->>> "+file_1)
        #file_1 dosyasındaki verison değeri eklentinin hangi lider versionu ile çalışacağını belirler. Eklenti versiyonu ile aynı olmak zorunda değildir.
        self.util.replace(file_1, "<version>1.0.0</version>", "<version>"+str(version)+"</version>")
        # mvn -N versions:update-child-modules

        file_2 = self.plugin_path.format(plugin_name)+"/lider-{}/pom.xml".format(plugin_name)
        self.util.replace(file_2, "<version>1.0.0</version>", "<version>"+str(version)+"</version>")
        print(file_2)



