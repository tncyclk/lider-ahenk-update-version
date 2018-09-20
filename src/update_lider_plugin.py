#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from util import Util

class UpdateLiderPlugin(object):
    def __init__(self):
        super(UpdateLiderPlugin, self).__init__()
        self.util = Util()
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')

    def change_version(self, data):
        plugin_name = data['plugin_name']
        version = data['plugin_version']
        plugin_cfg = data['plugin_cfg']
        lider_version = data['lider_version']

        file_1 = self.plugin_path.format(plugin_name)+"/pom.xml"

        #file_1 dosyasındaki verison değeri eklentinin hangi lider versionu ile çalışacağını belirler. Eklenti versiyonu ile aynı olmak zorunda değildir.

        self.util.replace(file_1, "<version>1.0.0</version>", "<version>"+str(lider_version)+"</version>")
        self.util.execute_command("mvn -N versions:update-child-modules", self.plugin_path.format(plugin_name))
        # mvn -N versions:update-child-modules

        file_2 = self.plugin_path.format(plugin_name)+"/lider-{}/pom.xml".format(plugin_name)
        self.util.replace(file_2, "<Bundle-Version>1.0.0</Bundle-Version>", "<Bundle-Version>"+str(version)+"</Bundle-Version>")

        ## Eğer eklentinin db projesi tasnımlanmış ise lider-script/pom.xml dosyasındaki db versiyonu güncellenmelidir.

        contents = self.util.read_file(file_2.format(plugin_name))
        if 'lider-{}-db'.format(plugin_name) in contents:
            self.util.replace(file_2, "<version>1.0.0</version>", "<version>" + str(version) + "</version>")
        else:
            print("eklentiye ait db projesi tanımlanmamıştır...!!")

        file_3 = self.plugin_path.format(plugin_name)+"/lider-{}-db/pom.xml".format(plugin_name)
        if self.util.is_exist(file_3) is True:
            self.util.replace(file_3, "<version>1.0.0</version>", "<version>" + str(plugin_name) + "</version>")
        else:
            print(file_3 + " dosyası bulunamadı")

        #lider-ahenk-script-plugin/lider-script/src/main/resources/tr.org.liderahenk.script.cfg dosyasındaki versiyon güncellenir.
        file_4 = self.plugin_path.format(plugin_name)+"/lider-{}/src/main/resources/".format(plugin_name) + plugin_cfg
        self.util.replace(file_4, "plugin.version = 1.0.0", "plugin.version = "+str(version))


