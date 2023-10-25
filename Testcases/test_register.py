import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.RegisterPage import RegisterPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Register:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_register(self):
        self.logger.info("   Test_Register")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.rp = RegisterPage(self.driver)
        self.rp.clickRegisterlink()
        self.logger.info("   Registration Process has been started")
        self.logger.info("   Entering the details")
        self.rp.enterFirstName("Priyanka")
        self.rp.enterLastName("PR")
        self.rp.enterAddress("#1234")
        self.rp.enterCityName("BLR")
        self.rp.enterStateName("Karnataka")
        self.rp.enterZipCode("50008")
        self.rp.enterPhoneNum("0818222222")
        self.rp.enterSSN("1234567891")
        self.rp.enterUserName("priyanka")
        self.rp.enterPassword("16012000")
        self.rp.enterConfirmPassword("16012000")
        self.rp.clickRegister()
        self.logger.info("   Registration Process Completed")

        textMatch = self.driver.find_element(By.XPATH, "//p[contains(text(),'Your account was created "
                                                       "successfully. ""You are now')]").text
        if 'Your account was created successfully. You are now logged in.' in textMatch:
            assert True
            self.rp.clickLogout()
            self.logger.info("   Registration Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_register.png")
            self.logger.error("   Test Unsuccessful")
            assert False
