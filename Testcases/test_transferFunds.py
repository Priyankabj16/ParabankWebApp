import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AccountsOverviewPage import AccountsOverview
from pageObjects.TransferFundsPage import TransferFunds
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_TransferFunds:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_transferFunds(self):
        self.logger.info("   Test_TransferFunds")
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
        value1 = acc_num1.text
        acc_num2 = self.ao.Account2()
        value2 = acc_num2.text

        self.logger.info("   Transferring Funds process has been started")
        self.tf = TransferFunds(self.driver)
        self.tf.clickTransferFunds()
        self.logger.info("   Entering the required details")
        self.tf.enterAmount("100")
        self.tf.selectFromAccount(value1)
        self.tf.selectToAccount(value2)
        self.tf.clickTransfer()

        textMatch = self.driver.find_element(By.XPATH, "//h1[normalize-space()="
                                                       "'Transfer Complete!']").text

        if 'Transfer Complete!' in textMatch:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Amount transferred Successfully")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_transferFunds.png")
            self.logger.error("   Test Unsuccessful")
            assert False
