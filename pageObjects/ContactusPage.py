from selenium.webdriver.common.by import By


class ContactUs:
    lnkContactus_xpath = "//a[normalize-space()='Contact Us']"
    name_xpath = "//input[@id='name']"
    email_xpath = "//input[@id='email']"
    phoneNum_xpath = "//input[@id='phone']"
    message_xpath = "//textarea[@id='message']"
    btnsend_xpath = "//input[@value='Send to Customer Care']"

    def __init__(self, driver):
        self.driver = driver

    def clickContactus(self):
        self.driver.find_element(By.XPATH, self.lnkContactus_xpath).click()

    def enterName(self, name):
        self.driver.find_element(By.XPATH, self.name_xpath).send_keys(name)

    def enterEmail(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enterPhoneNum(self, phoneNum):
        self.driver.find_element(By.XPATH, self.phoneNum_xpath).send_keys(phoneNum)

    def writeMessage(self, message):
        self.driver.find_element(By.XPATH, self.message_xpath).send_keys(message)

    def clickSendtoCustomerCare(self):
        self.driver.find_element(By.XPATH, self.btnsend_xpath).click()
