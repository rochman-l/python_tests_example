# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from group import Group
from contact import Contact


class TestGroupCreation():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(30)

  def teardown_method(self):
    self.driver.quit()
  
  def test_groupCreation(self):
    self.open_home_page()
    self.login(user_name = "admin", password= "secret")
    self.open_groups_list()
    self.create_group(Group("name", "hh", "ff"))
    self.open_groups_list()
    self.create_contact(Contact("nn", "ll"))
    self.return_to_home_page()

  def return_to_home_page(self):
    self.driver.find_element(By.LINK_TEXT, "home page").click()

  def create_contact(self, contact):
    self.driver.find_element(By.LINK_TEXT, "add new").click()
    self.driver.find_element(By.NAME, "firstname").click()
    self.driver.find_element(By.NAME, "firstname").send_keys(contact.f_name)
    self.driver.find_element(By.NAME, "lastname").click()
    self.driver.find_element(By.NAME, "lastname").send_keys(contact.l_name)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

  def create_group(self, group):
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
    self.driver.find_element(By.NAME, "submit").click()

  def open_groups_list(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def login(self, user_name, password):
    self.driver.find_element(By.NAME, "user").click()
    self.driver.find_element(By.NAME, "user").send_keys(user_name)
    self.driver.find_element(By.NAME, "pass").click()
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_home_page(self):
    self.driver.get("http://127.0.0.1/addressbook/")
  
