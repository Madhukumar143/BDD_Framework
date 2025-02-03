from selenium.webdriver.common.by import By
from features.Pages.Basepage import BasePage

class Accountpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    edit_your_account_option_linktext = "Edit your account information"
    account_created_confirmation_xpath= "//div[@id='content']/child::h1"



    def display_status_of_edit_account(self):
        return self.check_display_status("edit_your_account_option_linktext",self.edit_your_account_option_linktext)
        #return self.driver.find_element(By.LINK_TEXT,self.edit_your_account_option_link_text).is_displayed()

    def check_status_of_account_registration(self,exp_text):
        return self.retrieve_text("account_created_confirmation_xpath",self.account_created_confirmation_xpath).__eq__(exp_text)
        #return self.driver.find_element(By.XPATH,self.account_created_confirmation_xpath).text.__eq__(exp_text)

