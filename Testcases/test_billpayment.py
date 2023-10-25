import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountsOverviewPage import AccountsOverview
from pageObjects.BillpaymentPage import Billpayment
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_BillPayment:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_billpayment(self):
        self.logger.info("   Test_BillPayment")
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

        self.bp = Billpayment(self.driver)
        self.logger.info("   Payment Process has been started")
        self.bp.clickBillpay()
        self.logger.info("   Entering the Payee Details")
        self.bp.enterpPayeeName("Sid")
        self.bp.enterAddress("#169")
        self.bp.enterCityName("Mys")
        self.bp.enterStateName("KA")
        self.bp.enterZipCode("10001")
        self.bp.enterPhoneNum("0818266666")
        self.bp.enterAccountNum("75756565411")
        self.bp.enterVerifyAccountNum("75756565411")
        self.bp.enterAmount("50")
        self.bp.fromAccount(value1)
        self.bp.clickSendPayment()

        textMatch = self.driver.find_element(By.XPATH, "//p[contains(text(),'Your account was created "
                                                       "successfully. ""You are now')]").text
        if 'Your account was created successfully. You are now logged in.' in textMatch:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Payment Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_billpayment.png")
            self.logger.error("   Test Unsuccessful")
            assert False
