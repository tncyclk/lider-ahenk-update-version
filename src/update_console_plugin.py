#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Tuncay ÇOLAK <tuncay.colak@tubitak.gov.tr>

import os
from util import Util

class UpdateConsolePlugin(object):
    def __init__(self):
        super(UpdateConsolePlugin, self).__init__()
        self.util = Util()
        self.plugin_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../plugins/lider-ahenk-{}-plugin')

    def change_version(self, plugin_name, version):
        file_1 = self.plugin_path.format(plugin_name)+"/lider-console-{}/META-INF/MANIFEST.MF".format(plugin_name)
        self.util.replace(file_1, "Bundle-Version: 1.0.0", "Bundle-Version: 1.0.0.qualifier")

        file_2 = self.plugin_path.format(plugin_name)+"/lider-console-{}/plugin.xml".format(plugin_name)
        self.util.replace(file_2, 'pluginVersion="1.0.0"', 'pluginVersion="{}"'.format(str(version)))

        file_3 = self.plugin_path.format(plugin_name)+"/lider-console-{}/pom.xml".format(plugin_name)
        self.util.replace(file_3, "</parent>", "</parent>\n\t<version>1.0.0-SNAPSHOT</version>")

        file_4 = self.plugin_path.format(plugin_name)+"/lider-console-{}-feature/pom.xml".format(plugin_name)
        self.util.replace(file_4, "</parent>", "</parent>\n\t<version>1.0.0-SNAPSHOT</version>")

        file_5 = self.plugin_path.format(plugin_name)+"/lider-console-{}-feature/feature.xml".format(plugin_name)
        self.util.replace(file_5, 'version="1.0.0"', 'version="1.0.0.qualifier"')

        file_6 = self.plugin_path.format(plugin_name) + "/lider-console-{}-feature/feature.xml".format(plugin_name)
        self.util.replace(file_6, 'version="1.0.0"', 'version="1.0.0.qualifier"')

        ## Constants.java dosyasındaki PLUGIN_VERSİON değeri değiştirilir.

        if plugin_name == "script":
            file = self.plugin_path.format(plugin_name)+"/lider-console-script/src/tr/org/liderahenk/script/constants/ScriptConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "backup":
            file = self.plugin_path.format(plugin_name) + "/lider-console-backup/src/tr/org/liderahenk/backup/constants/BackupConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "antivirus":
            file = self.plugin_path.format(plugin_name) + "/lider-console-antivirus/src/tr/org/liderahenk/antivirus/constants/AntivirusConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "browser":
            file = self.plugin_path.format(plugin_name) + "/lider-console-browser/src/tr/org/liderahenk/browser/constants/BrowserConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "conky":
            file = self.plugin_path.format(plugin_name) + "/lider-console-conky/src/tr/org/liderahenk/conky/constants/ConkyConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        # elif plugin_name == "disk-limit":
        #     file = self.plugin_path.format(plugin_name) + "/lider-console-disk-limit/src/tr/org/liderahenk/disklimit/constants/DiskLimitConstants.java"
        #     self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "disk-quota":
            file = self.plugin_path.format(plugin_name) + "/lider-console-disk-quota/src/tr/org/liderahenk/disk/quota/constants/DiskQuotaConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "firewall":
            file = self.plugin_path.format(plugin_name) + "/lider-console-firewall/src/tr/org/liderahenk/firewall/constants/FirewallConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "local-user":
            file = self.plugin_path.format(plugin_name) + "/lider-console-local-user/src/tr/org/liderahenk/localuser/constants/LocalUserConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "login-manager":
            file = self.plugin_path.format(plugin_name) + "/lider-console-login-manager/src/tr/org/liderahenk/loginmanager/constants/LoginManagerConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        # elif plugin_name == "manage-root":
        #     file = self.plugin_path.format(plugin_name) + "/lider-console-manage-root/src/tr/org/liderahenk/manageroot/constants/ManageRootConstants.java"
        #     self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        # elif plugin_name == "network-inventory":
        #     file = self.plugin_path.format(plugin_name) + "/lider-console-network-inventory/src/tr/org/liderahenk/network/inventory/constants/NetworkInventoryConstants.java"
        #     self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "network-manager":
            file = self.plugin_path.format(plugin_name) + "/lider-console-network-manager/src/tr/org/liderahenk/networkmanager/constants/NetworkManagerConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "package-manage":
            file = self.plugin_path.format(plugin_name) + "/lider-console-package-manage/src/tr/org/liderahenk/packagemanager/constants/PackageManagerConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "password":
            file = self.plugin_path.format(plugin_name) + "/lider-console-password/src/tr/org/liderahenk/password/constants/PasswordConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "remote-access":
            file = self.plugin_path.format(plugin_name) + "/lider-console-remote-access/src/tr/org/liderahenk/remote/access/constants/RemoteAccessConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "resource-usage":
            file = self.plugin_path.format(plugin_name) + "/lider-console-resource-usage/src/tr/org/liderahenk/resourceusage/constants/ResourceUsageConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "restore":
            file = self.plugin_path.format(plugin_name) + "/lider-console-restore/src/tr/org/liderahenk/restore/constants/RestoreConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "rsyslog":
            file = self.plugin_path.format(plugin_name) + "/lider-console-rsyslog/src/tr/org/liderahenk/rsyslog/constants/RsyslogConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "screensaver":
            file = self.plugin_path.format(plugin_name) + "/lider-console-screensaver/src/tr/org/liderahenk/screensaver/constants/ScreensaverConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "screenshot":
            file = self.plugin_path.format(plugin_name) + "/lider-console-screenshot/src/tr/org/liderahenk/screenshot/constants/ScreenshotConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "service":
            file = self.plugin_path.format(plugin_name) + "/lider-console-service/src/tr/org/liderahenk/service/constants/ServiceConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "sudoers":
            file = self.plugin_path.format(plugin_name) + "/lider-console-sudoers/src/tr/org/liderahenk/sudoers/constants/SudoersConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "usb-ltsp":
            file = self.plugin_path.format(plugin_name) + "/lider-console-usb-ltsp/src/tr/org/liderahenk/usb/ltsp/constants/UsbLtspConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "usb":
            file = self.plugin_path.format(plugin_name) + "/lider-console-usb/src/tr/org/liderahenk/usb/constants/UsbConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "user-privilege":
            file = self.plugin_path.format(plugin_name) + "/lider-console-user-privilege/src/tr/org/liderahenk/user/privilege/constants/UserPrivilegeConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "wol":
            file = self.plugin_path.format(plugin_name) + "/lider-console-wol/src/tr/org/liderahenk/wol/constants/WolConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        elif plugin_name == "ldap-login":
            file = self.plugin_path.format(plugin_name) + "/lider-console-ldap-login/src/tr/org/liderahenk/ldaplogin/constants/LdapLoginConstants.java"
            self.util.replace(file, 'PLUGIN_VERSION = "1.0.0"', 'PLUGIN_VERSION = "{}"'.format(str(version)))

        else:
            print("Eklenti bulunamadı")



