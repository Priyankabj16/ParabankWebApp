import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.ContactusPage import ContactUs
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ContactUs:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_requestLoan(self):
        self.logger.info("   Test_ContactUs")
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

        self.cu = ContactUs(self.driver)
        self.cu.clickContactus()
        self.logger.info("   Trying to Contact the administration")
        self.logger.info("   Entering personal details")
        self.cu.enterName("Arr")
        self.cu.enterEmail("arr@gmail.com")
        self.cu.enterPhoneNum("081827777")
        self.logger.info("   Stating the problem to  the administration")
        self.cu.writeMessage("Login isn't working")
        self.logger.info("   Sending the problem statement")
        self.cu.clickSendtoCustomerCare()

        textMatch = self.driver.find_element(By.XPATH, "//p[contains(text(),'A Customer Care "
                                                       "Representative will be contacting ')]").text
        if 'A Customer Care Representative will be contacting you.' in textMatch:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Test Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_contactus.png")
            self.logger.error("   Test Unsuccessful")
            assert False
            