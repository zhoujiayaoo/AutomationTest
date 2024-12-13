# -*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from base.web_ui.oceanCoatiProject.web_ui_oceanCoatiProject_client import WEB_UI_OceanCoatiProject_Client
from page_objects.web_ui.oceanCoatiProject.pages.indexPage import IndexPage
from common.hamcrest.hamcrest import assert_that

class TestIndex:
    def setup_class(self):
        self.oceanCoatiProjectClient = WEB_UI_OceanCoatiProject_Client()
        self.indexPage=IndexPage(self.oceanCoatiProjectClient.browserOperator)

    def test_search_empty_kw(self):
        self.indexPage.search_kw('')
        assert_that(self.indexPage.getElements().title.wait_expected_value).is_equal_to(self.oceanCoatiProjectClient.browserOperator.getTitle())

    def test_search_kw(self):
        self.indexPage.search_kw('apitest')
        assert_that('apitest_百度搜索').is_equal_to(self.oceanCoatiProjectClient.browserOperator.getTitle())

    def teardown_class(self):
        self.oceanCoatiProjectClient.browserOperator.close()