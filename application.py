from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)

    def create_contact(self, contact):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "add new").click()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact.f_name)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact.l_name)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def create_group(self, group):
        driver = self.driver
        self.open_groups_list()
        driver.find_element(By.NAME, "new").click()
        driver.find_element(By.NAME, "group_name").click()
        driver.find_element(By.NAME, "group_name").send_keys(group.name)
        driver.find_element(By.NAME, "group_header").click()
        driver.find_element(By.NAME, "group_header").send_keys(group.header)
        driver.find_element(By.NAME, "group_footer").click()
        driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        driver.find_element(By.NAME, "submit").click()
        self.open_groups_list()

    def open_groups_list(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "groups").click()

    def login(self, user_name, password):
        driver = self.driver
        self.open_home_page()
        driver.find_element(By.NAME, "user").click()
        driver.find_element(By.NAME, "user").send_keys(user_name)
        driver.find_element(By.NAME, "pass").click()
        driver.find_element(By.NAME, "pass").send_keys(password)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_home_page(self):
        driver = self.driver
        driver.get("http://127.0.0.1/addressbook/")

    def return_to_home_page(self):
        driver = self.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

    def destroy(self):
        driver = self.driver
        driver.quit()