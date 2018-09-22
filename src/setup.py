#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import ezodf
from util import Util
from git_operation import GitConfig
from update_lider_plugin import UpdateLiderPlugin
from update_console_plugin import UpdateConsolePlugin
from update_ahenk_plugin import UpdateAhenkPlugin

class VersionManager(object):
    def __init__(self):
        super(VersionManager, self).__init__()
        self.util = Util()
        self.git = GitConfig()
        self.lider_plugin = UpdateLiderPlugin()
        self.console_plugin = UpdateConsolePlugin()
        self.ahenk_plugin = UpdateAhenkPlugin()

        self.project_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/')
        self.plugin_package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../packages/{}')
        self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_list')
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')
        self.plugin_deb_path = "/tmp/lider-ahenk-{0}-plugin/ahenk-{0}_{1}_amd64.deb"
        self.plugin_lider_jar_path = "/tmp/lider-ahenk-{0}-plugin/lider-{0}-1.2.jar"
        self.plugin_db_jar = "lider-{0}-db-{1}.jar"
        self.log_file = self.plugin_list_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../version.log')

        self.plugin_version_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_version.ods')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/'))
        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../packages')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../packages/'))

    def version_manager(self, data):
        self.git.install_project(data['plugin_url'])
        self.git.create_tag(data['plugin_name'], data['plugin_version'])
        self.git.create_branch(data['plugin_name'], data['plugin_version'])
        self.lider_plugin.change_version(data)
        self.console_plugin.change_version(data['plugin_name'], data['plugin_version'])
        self.ahenk_plugin.change_version(data['plugin_name'], data['plugin_version'])
        self.copy_packages(data)

        print("--------->>>>>>>>> ["+str(data["plugin_name"])+"] eklentisinin [" + str(data["plugin_version"])+"] versiyonu tamamlandı....!!")
        self.util.write_file(self.log_file, "["+str(data["plugin_name"])+"] eklentisinin [" + str(data["plugin_version"])+"] versiyonu tamamlandı....!!\n")

    def copy_packages(self, data):
        self.util.create_directory(self.plugin_package_path.format(data['plugin_name']))
        self.util.copy_file(self.plugin_deb_path.format(data['plugin_name'], data['plugin_version']), self.plugin_package_path.format(data['plugin_name']))
        self.util.copy_file(self.plugin_lider_jar_path.format(data['plugin_name']), self.plugin_package_path.format(data['plugin_name']))

        file_db = self.plugin_path.format(data['plugin_name']) + "/lider-{}-db/target".format(data['plugin_name'])
        if self.util.is_exist(file_db):
            self.util.copy_file(file_db+"/"+self.plugin_db_jar.format(data['plugin_name'], data['plugin_version']), self.plugin_package_path.format(data['plugin_name']))
            print(data['plugin_name']+" eklentisine ait db projesi tanımlanmıştır")
        else:
            print(data['plugin_name']+" eklentinin db projesi tanımlanmamıştır....!!!!")

        cmd_zip = "zip -r lider-{0}-console_{1}.zip ."
        self.util.execute_command(cmd_zip.format(data['plugin_name'], data['plugin_version']), self.plugin_path.format(data['plugin_name'])+"/lider-console-{0}-feature/target/site".format(data['plugin_name']))
        self.util.copy_file(self.plugin_path.format(data['plugin_name'])+"/lider-console-{0}-feature/target/site/lider-{0}-console_{1}.zip".format(data['plugin_name'], data['plugin_version']), self.plugin_package_path.format(data['plugin_name']))

    def read_file(self):
        ezodf.config.set_table_expand_strategy('all')
        doc = ezodf.opendoc(self.plugin_version_path)
        sheet = doc.sheets[0]

        print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
        for sheet in doc.sheets:
            print("-" * 40)
            print("   Sheet name : '%s'" % sheet.name)
            print("Size of Sheet : (rows=%d, cols=%d)" % (sheet.nrows(), sheet.ncols()))

        plugin_size = sheet.nrows() + 1
        for i in range(2, plugin_size):
            plugin_data = {
                'plugin_name': sheet['A{}'.format(i)].value,
                'plugin_version': sheet['B{}'.format(i)].value,
                'lider_version': sheet['C{}'.format(i)].value,
                'plugin_url': sheet['D{}'.format(i)].value,
                'plugin_cfg': sheet['E{}'.format(i)].value
            }
            self.version_manager(plugin_data)

if __name__ == '__main__':
    app = VersionManager()
    app.read_file()