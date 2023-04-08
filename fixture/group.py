from sys import maxsize

from selenium.webdriver.common.by import By

from model.group import Group


class GroupHelper:
    def __init__(self, app):
        self.app = app

    def create(self, group):
        driver = self.app.driver
        self.open_groups_page()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_page()
        self.group_cache = None

    def modify(self, group):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        self.fill_group_form(group)
        driver.find_element(By.NAME, "update").click()
        self.open_groups_page()
        self.group_cache = None

    def fill_group_form(self, group):
        driver = self.app.driver
        driver.find_element(By.NAME, "edit").click()
        if group.name is not None:
            self.type("group_name", group.name)
        if group.header is not None:
            self.type("group_header", group.header)
        if group.footer is not None:
            self.type("group_footer", group.footer)

    def type(self, field_name, text):
        driver = self.app.driver
        driver.find_element(By.NAME, field_name).click()
        driver.find_element(By.NAME, field_name).clear()
        driver.find_element(By.NAME, field_name).send_keys(text)

    def modify_first(self, new_group_data):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element(By.NAME, "edit").click()
        self.fill_group_form(self, new_group_data)
        driver.find_element(By.NAME, "update").click()
        self.open_groups_page()
        self.group_cache = None

    def delete(self):
        driver = self.app.driver
        self.open_groups_page()
        self.select_first_group()
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def delete_by_index(self, index):
        driver = self.app.driver
        self.open_groups_page()
        self.select_group_by_index(index)
        driver.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_first_group(self):
        driver = self.app.driver
        driver.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        driver = self.app.driver
        driver.find_elements(By.NAME, "selected[]")[index].click()

    def open_groups_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        driver = self.app.driver
        self.open_groups_page()
        return len(driver.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            driver = self.app.driver
            self.open_groups_page()
            self.group_cache = []
            for element in driver.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)

