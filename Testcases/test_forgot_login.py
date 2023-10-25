import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.ForgotLoginPage import ForgotLogin
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_ForgotLogin:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_register(self):
        self.logger.info("   Test_ForgotLogin")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.sp = ForgotLogin(self.driver)
        self.logger.info("   Entering the required details")
        self.sp.enterFirstName("Priyanka")
        self.sp.enterLastName("PR")
        self.sp.enterAddress("#1234")
        self.sp.enterCityName("BLR")
        self.sp.enterStateName("Karnataka")
        self.sp.enterZipCode("50008")
        self.sp.enterSSN("1234567891")
        self.sp.clickFindMyLogin()
        self.logger.info("   Finding the login information")

        textMatch = self.driver.find_element(By.CSS_SELECTOR, "//p[contains(text(),'Your login "
                                                              "information was located successfully. Y')]").text
        if 'Your login information was located successfully. You are now logged in. ' in textMatch:
            assert True
            self.sp.clickLogout()
            self.logger.info("   Test Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgot_login.png")
            self.logger.error("   Test Unsuccessful")
            assert False
