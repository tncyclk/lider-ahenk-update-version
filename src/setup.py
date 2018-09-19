#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
import ezodf
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

        self.plugin_version_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../conf/plugin_version.ods')

        if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins')):
            os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/'))

    def version_manager(self, data):
        print(data)
        self.git.install_project(data['plugin_url'])
        # self.git.create_tag(data['plugin_name'], data['plugin_version'])
        # self.git.create_branch(data['plugin_name'], data['plugin_version'])

        self.update_version.set_version(data['plugin_name'], data['plugin_version'])

    def read_file(self):
        ezodf.config.set_table_expand_strategy('all')
        doc = ezodf.opendoc(self.plugin_version_path)
        sheet = doc.sheets[0]

        # print("Spreadsheet contains %d sheet(s)." % len(doc.sheets))
        # for sheet in doc.sheets:
        #     print("-" * 40)
        #     print("   Sheet name : '%s'" % sheet.name)
        #     print("Size of Sheet : (rows=%d, cols=%d)" % (sheet.nrows(), sheet.ncols()))
        # print(sheet.nrows())

        plugin_size = sheet.nrows() + 1
        for i in range(2, plugin_size):
            plugin_data = {
                'plugin_name': sheet['A{}'.format(i)].value,
                'plugin_version': sheet['B{}'.format(i)].value,
                'lider_version': sheet['C{}'.format(i)].value,
                'plugin_url': sheet['D{}'.format(i)].value
            }
            self.version_manager(plugin_data)


if __name__ == '__main__':
    app = VersionManager()
    app.read_file()