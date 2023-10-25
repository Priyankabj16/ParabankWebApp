from selenium.webdriver.common.by import By


class AccountsOverview:
    lnkAccountsOverview_xpath = "//*[@id='leftPanel']/ul/li[2]/a"
    lnkAcc1_xpath = "//*[@id='accountTable']/tbody/tr[1]/td[1]/a"
    balanceAcc1_xpath = "//td[@id='balance']"
    lnkAcc2_xpath = "//*[@id='accountTable']/tbody/tr[2]/td[1]/a"
    balanceAcc2_xpath = "//td[@id='balance']"
    totalBalance_xpath = "//tbody/tr[3]/td[2]"

    def __init__(self, driver):
        self.driver = driver

    def clickAccountsOverview(self):
        self.driver.find_element(By.XPATH, self.lnkAccountsOverview_xpath).click()

    def Account1(self):
        self.driver.find_element(By.XPATH, self.lnkAcc1_xpath)

    def BalanceAccount1(self):
        self.driver.find_element(By.XPATH, self.balanceAcc1_xpath)

    def Account2(self):
        self.driver.find_element(By.XPATH, self.lnkAcc2_xpath)

    def BalanceAccount2(self):
        self.driver.find_element(By.XPATH, self.balanceAcc2_xpath)

    def clickTotalBalance(self):
        self.driver.find_element(By.XPATH, self.totalBalance_xpath)

