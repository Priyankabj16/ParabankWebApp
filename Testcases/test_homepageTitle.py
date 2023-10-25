import pytest
import faulthandler
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_HomePageTitle:
    faulthandler.disable()
    baseURL = ReadConfig.getbaseURL()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_HomePageTitle(self):
        self.logger.info("   Test_HomePageTitle")
        self.logger.info("   Launching Browser")
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.exp_title = "ParaBank | Welcome | Online Banking"
        if self.driver.title == self.exp_title:
            assert True
            self.driver.close()
            self.logger.info("   Test Successful")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePageTitle.png")
            self.logger.error("   Test Unsuccessful")
            self.driver.close()
            assert False
