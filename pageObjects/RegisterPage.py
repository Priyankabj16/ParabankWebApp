from selenium.webdriver.common.by import By


class RegisterPage:
    lnkRegister_xpath = "//a[normalize-space()='Register']"
    firstName_xpath = "//input[@id='customer.firstName']"
    lastName_xpath = "//input[@id='customer.lastName']"
    address_xpath = "//input[@id='customer.address.street']"
    cityName_xpath = "//input[@id='customer.address.city']"
    stateName_xpath = "//input[@id='customer.address.state']"
    zipcode_xpath = "//input[@id='customer.address.zipCode']"
    phoneNum_xpath = "//input[@id='customer.phoneNumber']"
    ssnNum_xpath = "//input[@id='customer.ssn']"
    username_xpath = "//input[@id='customer.username']"
    password_xpath = "//input[@id='customer.password']"
    confirmPassword_xpath = "//input[@id='repeatedPassword']"
    btnRegister_xpath = "//input[@value='Register']"
    btnlogout_xpath = "//a[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver

    def clickRegisterlink(self):
        self.driver.find_element(By.XPATH, self.lnkRegister_xpath).click()

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

    def enterPhoneNum(self, num):
        self.driver.find_element(By.XPATH, self.phoneNum_xpath).send_keys(num)

    def enterSSN(self, ssn):
        self.driver.find_element(By.XPATH, self.ssnNum_xpath).send_keys(ssn)

    def enterUserName(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def enterConfirmPassword(self, password):
        self.driver.find_element(By.XPATH, self.confirmPassword_xpath).send_keys(password)

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.btnRegister_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btnlogout_xpath).click()
