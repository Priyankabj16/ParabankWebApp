import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AccountsOverviewPage import AccountsOverview
from pageObjects.RequestLoanPage import RequestLoan
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_RequestLoan:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_requestLoan(self):
        self.logger.info("   Test_RequestLoan")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        self.logger.info("   Entering the login details")
        self.lp.enterUserName("priyanka")
        self.lp.enterPassword("16012000")
        self.lp.clickLogin()
        self.logger.info("   Successfully logged in")

        self.ao = AccountsOverview(self.driver)
        self.ao.clickAccountsOverview()
        acc_num1 = self.ao.Account1()
        value1 = acc_num1.get_attribute('ng-scope')
        acc_num2 = self.ao.Account2()
        value2 = acc_num2.get_attribute('ng-scope')

        self.logger.info("   Requesting for Loan process has been started")
        self.rl = RequestLoan(self.driver)
        self.rl.clickRequestLoan()
        self.logger.info("   Entering the required details")
        self.rl.enterAmount("10000")
        self.rl.enterDownPayment("100")
        self.rl.selectFromAccount(value1)
        self.rl.clickApplyNow()

        textMatch = self.driver.find_element(By.XPATH, "//p[normalize-space()='Congratulations, "
                                                       "your loan has been approved.']").text
        if 'Congratulations, your loan has been approved.' in textMatch:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Loan has been Approved")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_requestLoan.png")
            self.logger.error("   Test Unsuccessful")
            assert False
            