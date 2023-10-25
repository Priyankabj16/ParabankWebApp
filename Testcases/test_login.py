import pytest
import faulthandler
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_Login:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_login(self):
        self.logger.info("   Test_Login")
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
        self.exp_url = "https://parabank.parasoft.com/parabank/overview.htm"
        if self.driver.current_url == self.exp_url:
            assert True
            self.lp.clickLogout()
            self.logger.info("   Successfully logged in")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.logger.error("   Test Unsuccessful")
            assert False
