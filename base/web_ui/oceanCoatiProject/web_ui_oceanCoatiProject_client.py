# -*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from base.web_ui.oceanCoatiProject.web_ui_oceanCoatiProject_read_config import WEB_UI_OceanCoatiProject_Read_Config
from base.read_web_ui_config import Read_WEB_UI_Config
from common.selenium.browserOperator import BrowserOperator
from common.selenium.driverTool import DriverTool
class WEB_UI_OceanCoatiProject_Client:
    def __init__(self):
        self.config=Read_WEB_UI_Config().web_ui_config
        self.oceanCoatiProjectConfig=WEB_UI_OceanCoatiProject_Read_Config().config

        self.driver = DriverTool.get_driver(self.config.selenium_hub, self.config.current_browser)
        self.driver.get(self.oceanCoatiProjectConfig.web_host + '/')
        self.browserOperator = BrowserOperator(self.driver)
