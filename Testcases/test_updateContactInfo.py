import pytest
import faulthandler
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.UpdateContactInfoPage import UpdateContactInfo
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_UpdateContact_Info:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_updateContactInfo(self):
        self.logger.info("   Test_UpdateContact_Info")
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

        self.uc = UpdateContactInfo(self.driver)
        self.logger.info("   Updating the Contact information")
        self.uc.clickUpdateContactInfo()
        self.logger.info("   Making the required changes")
        self.uc.enterAddress("#12345")
        self.uc.enterPhoneNum("0818222221")
        self.uc.clickUpdateProfile()

        textMatch = self.driver.find_element(By.XPATH, "//h1[normalize-space()='Profile Updated']").text
        if 'Profile Updated' in textMatch:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Profile Updated")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_updateContactInfo.png")
            self.logger.error("   Test Unsuccessful")
            assert False
