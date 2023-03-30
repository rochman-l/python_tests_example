# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from group import Group
from contact import Contact
from application import Application

class TestGroupCreation():
    def setup_method(self):
        self.app = Application()

    def teardown_method(self):
        self.app.destroy()

    def test_group_creation(self):
        self.app.login(user_name = "admin", password= "secret")
        self.app.create_group(Group("name", "hh", "ff"))

    def test_contact_creation(self):
        self.app.login(user_name = "admin", password= "secret")
        self.app.create_contact(Contact("nn", "ll"))
        self.app.return_to_home_page()



  
