#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from util import Util

class UpdateAhenkPlugin(object):
    def __init__(self):
        super(UpdateAhenkPlugin, self).__init__()
        self.util = Util()
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')

    def change_version(self, plugin_name, version):
        file_1 = self.plugin_path.format(plugin_name)+"/ahenk-{}/debian/changelog".format(plugin_name)
        self.util.replace(file_1, '(1.0.0)', '('+str(version)+')')

        file_2 = self.plugin_path.format(plugin_name)+"/ahenk-{}/debian/control".format(plugin_name)
        self.util.replace(file_2, 'Version: 1.0.0', 'Version: {}'.format(str(version)))

        file_3 = self.plugin_path.format(plugin_name)+"/ahenk-{0}/{0}/main.py".format(plugin_name)
        self.util.replace(file_3, "1.0.0", str(version))

        self.util.execute_command('/bin/bash scripts/build-plugin.sh', self.plugin_path.format(plugin_name))

