from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class RequestLoan:
    lnkRequestLoan_xpath = "//a[normalize-space()='Request Loan']"
    amount_xpath = "//input[@id='amount']"
    downPayment_xpath = "//input[@id='downPayment']"
    drpFromAccount_xpath = "//select[@id='fromAccountId']"
    btnApplyNow_xpath = "//input[@value='Apply Now']"

    def __init__(self, driver):
        self.driver = driver

    def clickRequestLoan(self):
        self.driver.find_element(By.XPATH, self.lnkRequestLoan_xpath).click()

    def enterAmount(self, amount):
        self.driver.find_element(By.XPATH, self.amount_xpath).send_keys(amount)

    def enterDownPayment(self, amount):
        self.driver.find_element(By.XPATH, self.downPayment_xpath).send_keys(amount)

    def selectFromAccount(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpFromAccount_xpath))
        drp.select_by_visible_text(value)

    def clickApplyNow(self):
        self.driver.find_element(By.XPATH, self.btnApplyNow_xpath).click()
