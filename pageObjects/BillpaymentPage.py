from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Billpayment:
    lnkbillpay_xpath = "//a[normalize-space()='Bill Pay']"
    payeeName_xpath = "//input[@name='payee.name']"
    address_xpath = "//input[@name='payee.address.street']"
    cityName_xpath = "//input[@name='payee.address.city']"
    stateName_xpath = "//input[@name='payee.address.state']"
    zipcode_xpath = "//input[@name='payee.address.zipCode']"
    phoneNum_css = "#c88e2466-8740-4062-9618-e1c105a8bc55"
    accountNum_xpath = "//input[@name='payee.accountNumber']"
    verifyAccountNum_xpath = "//input[@name='verifyAccount']"
    amount_xpath = "//input[@name='amount']"
    drpFromAccount_xpath = "//select[@name='fromAccountId']"
    btnSendPyment_xpath = "//input[@value='Send Payment']"

    def __init__(self, driver):
        self.driver = driver

    def clickBillpay(self):
        self.driver.find_element(By.XPATH, self.lnkbillpay_xpath).click()

    def enterpPayeeName(self, name):
        self.driver.find_element(By.XPATH, self.payeeName_xpath).send_keys(name)

    def enterAddress(self, address):
        self.driver.find_element(By.XPATH, self.address_xpath).send_keys(address)

    def enterCityName(self, cityname):
        self.driver.find_element(By.XPATH, self.cityName_xpath).send_keys(cityname)

    def enterStateName(self, statename):
        self.driver.find_element(By.XPATH, self.stateName_xpath).send_keys(statename)

    def enterZipCode(self, zcode):
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(zcode)

    def enterPhoneNum(self, num):
        self.driver.find_element(By.CSS_SELECTOR, self.phoneNum_css).send_keys(num)

    def enterAccountNum(self, accNum):
        self.driver.find_element(By.XPATH, self.accountNum_xpath).send_keys(accNum)

    def enterVerifyAccountNum(self, accNum):
        self.driver.find_element(By.XPATH, self.verifyAccountNum_xpath).send_keys(accNum)

    def enterAmount(self, amount):
        self.driver.find_element(By.XPATH, self.amount_xpath).send_keys(amount)

    def fromAccount(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drpFromAccount_xpath))
        drp.select_by_visible_text(value)

    def clickSendPayment(self):
        self.driver.find_element(By.XPATH, self.btnSendPyment_xpath).click()
