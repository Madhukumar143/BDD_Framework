from selenium.webdriver.common.by import By

from features.Pages.Basepage import BasePage
from features.Pages.accountsPage import Accountpage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    email_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"

    def enter_email_adress(self,email_text):
        self.type_into_element("email_field_xpath",self.email_field_xpath,email_text)
        #self.driver.find_element(By.XPATH,self.email_field_xpath).send_keys(email_text)

    def enter_the_password(self,password_text):
        self.type_into_element("password_field_xpath",self.password_field_xpath,password_text)
        #self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_text)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath",self.login_button_xpath)
        #self.driver.find_element(By.XPATH,self.login_button_xpath).click()
        return Accountpage(self.driver)

    def display_status_of_warning_message(self,expected_warning_text):
        return self.retrieve_text("warning_message_xpath",self.warning_message_xpath).__contains__(expected_warning_text)
        #return self.driver.find_element(By.XPATH,self.warning_message_xpath).text.__contains__(expected_warning_text)