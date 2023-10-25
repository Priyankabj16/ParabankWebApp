from selenium.webdriver.common.by import By


class UpdateContactInfo:
    lnkUpdateContactInfo = "//a[normalize-space()='Update Contact Info']"
    firstName_xpath = "//input[@id='customer.firstName']"
    lastName_xpath = "//input[@id='customer.lastName']"
    address_xpath = "//input[@id='customer.address.street']"
    cityName_xpath = "//input[@id='customer.address.city']"
    stateName_xpath = "//input[@id='customer.address.state']"
    zipcode_xpath = "//input[@id='customer.address.zipCode']"
    phoneNum_xpath = "//input[@id='customer.phoneNumber']"
    btnUpdateProfile_xpath = "//a[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver

    def clickUpdateContactInfo(self):
        self.driver.find_element(By.XPATH, self.lnkUpdateContactInfo).click()

    def enterFirstName(self, fname):
        self.driver.find_element(By.XPATH, self.firstName_xpath).clear()
        self.driver.find_element(By.XPATH, self.firstName_xpath).send_keys(fname)

    def enterLastName(self, lname):
        self.driver.find_element(By.XPATH, self.lastName_xpath).clear()
        self.driver.find_element(By.XPATH, self.lastName_xpath).send_keys(lname)

    def enterAddress(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).clear()
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def enterCityName(self, cityname):
        self.driver.find_element(By.XPATH, self.cityName_xpath).clear()
        self.driver.find_element(By.XPATH, self.cityName_xpath).send_keys(cityname)

    def enterStateName(self, statename):
        self.driver.find_element(By.XPATH, self.stateName_xpath).clear()
        self.driver.find_element(By.XPATH, self.stateName_xpath).send_keys(statename)

    def enterZipCode(self, zcode):
        self.driver.find_element(By.XPATH, self.zipcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(zcode)

    def enterPhoneNum(self, num):
        self.driver.find_element(By.XPATH, self.phoneNum_xpath).clear()
        self.driver.find_element(By.XPATH, self.phoneNum_xpath).send_keys(num)

    def clickUpdateProfile(self):
        self.driver.find_element(By.XPATH, self.btnUpdateProfile_xpath).clear()
        self.driver.find_element(By.XPATH, self.btnUpdateProfile_xpath).click()
