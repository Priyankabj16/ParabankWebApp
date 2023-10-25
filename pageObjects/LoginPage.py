from selenium.webdriver.common.by import By


class LoginPage:
    username_xpath = "//input[@name='username']"
    password_xpath = "//input[@name='password']"
    login_xpath = "//input[@value='Log In']"
    logout_xpath = "//a[normalize-space()='Log Out']"

    def __init__(self, driver):
        self.driver = driver

    def enterUserName(self, username):
        self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username)

    def enterPassword(self, password):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
