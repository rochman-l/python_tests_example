from selenium.webdriver.common.by import By


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def create(self, contact):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "add new").click()
        driver.find_element(By.NAME, "firstname").click()
        driver.find_element(By.NAME, "firstname").send_keys(contact.f_name)
        driver.find_element(By.NAME, "lastname").click()
        driver.find_element(By.NAME, "lastname").send_keys(contact.l_name)
        driver.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.return_to_home_page()

    def delete(self):
        driver = self.app.driver
        # driver.find_element(By.LINK_TEXT, "home").click()
        driver.find_element(By.NAME, "selected[]").click()
        driver.find_element(By.CSS_SELECTOR, "[onclick='DeleteSel()']").click()
        driver.switch_to.alert.accept()
        # self.return_to_home_page()

    def return_to_home_page(self):
        driver = self.app.driver
        driver.find_element(By.LINK_TEXT, "home page").click()

