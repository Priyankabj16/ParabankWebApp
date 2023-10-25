from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class TransferFunds:
    lnkTransferfunds_xpath = "//a[normalize-space()='Transfer Funds']"
    amount_xpath = "//input[@id='amount']"
    drpFromAccount_xpath = "//select[@id='fromAccountId']"
    drpToAccount_xpath = "//select[@id='toAccountId']"
    btnTransfer_xpth = "//input[@value='Transfer'"

    def __init__(self, driver):
        self.driver = driver

    def clickTransferFunds(self):
        self.driver.find_element(By.XPATH, self.lnkTransferfunds_xpath).click()

    def enterAmount(self, amount):
        self.driver.find_element(By.XPATH, self.amount_xpath).send_keys(amount)

    def selectFromAccount(self, value1):
        drp = Select(self.driver.find_element(By.XPATH, self.drpFromAccount_xpath))
        drp.select_by_visible_text(value1)

    def selectToAccount(self, value2):
        drp = Select(self.driver.find_element(By.XPATH, self.drpToAccount_xpath))
        drp.select_by_visible_text(value2)

    def clickTransfer(self):
        self.driver.find_element(By.XPATH, self.btnTransfer_xpth).click()
