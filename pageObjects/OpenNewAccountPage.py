from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class OpenNewAccountPage:
    lnkOpenNewAccount_xpath = "//a[normalize-space()='Open New Account']"
    drptypeofAccount_xpath = "//select[@id='type']"
    btnOpenNewAccount_xpath = "//input[@value='Open New Account']"

    def __init__(self, driver):
        self.driver = driver

    def clickOpenNewAccountlink(self):
        self.driver.find_element(By.XPATH, self.lnkOpenNewAccount_xpath).click()

    def typeOfAccount(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drptypeofAccount_xpath))
        drp.select_by_visible_text(value)

    def clickOpenNewAccount(self):
        self.driver.find_element(By.XPATH, self.btnOpenNewAccount_xpath).click()

