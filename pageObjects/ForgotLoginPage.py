from selenium.webdriver.common.by import By


class ForgotLogin:
    lnkForgotlogin_xpath = "//a[normalize-space()='Forgot login info?']"
    firstName_xpath = "//input[@id='firstName']"
    lastName_xpath = "//tbody/tr[2]/td[2]"
    address_xpath = "//input[@id='address.street']"
    cityName_xpath = "//input[@id='address.city']"
    stateName_xpath = "//input[@id='address.state']"
    zipcode_xpath = "//input[@id='address.zipCode']"
    ssnNum_xpath = "//input[@id='ssn']"
    btnFindmyLogin_xpath = "//input[@value='Find My Login Info']"
    btnlogout_xpath = "//a[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver

    def clickForgotLogin(self):
        self.driver.find_element(By.XPATH, self.lnkForgotlogin_xpath).click()

    def enterFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lname)

    def enterAddress(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def enterCityName(self, cityname):
        self.driver.find_element(By.XPATH, self.cityName_xpath).send_keys(cityname)

    def enterStateName(self, statename):
        self.driver.find_element(By.XPATH, self.stateName_xpath).send_keys(statename)

    def enterZipCode(self, zcode):
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(zcode)

    def enterSSN(self, ssn):
        self.driver.find_element(By.XPATH, self.ssnNum_xpath).send_keys(ssn)

    def clickFindMyLogin(self):
        self.driver.find_element(By.XPATH, self.btnFindmyLogin_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btnlogout_xpath).click()
