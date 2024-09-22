from selenium.webdriver.common.by import By

from features.Pages.Basepage import BasePage
from features.Pages.accountsPage import Accountpage


class Registerpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    firstname_locator_name = "firstname"
    lastname_locator_name = "lastname"
    email_field_locator_name = "email"
    telephone_field_locator_name = "telephone"
    password_field_locator_name = "password"
    confirm_password_locator_name = "confirm"
    privacy_policy_agree_locator_name = "agree"
    continue_button_xpath = "//input[@value='Continue']"
    newsletter_xpath_yes = "//label[normalize-space()='Yes']"
    newsletter_xpath_no = "//label[normalize-space()='No']"
    warning_msg_for_already_registered_email_xpath = "(//div[@id='account-register']/child::div)[1]"
    privacy_policy_warning_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    firstname_warning_xpath = "//input[@name='firstname']/following-sibling::div"
    lastname_warning_xpath = "//input[@name='lastname']/following-sibling::div"
    telephone_warning_xpath =  "//input[@name='telephone']/following-sibling::div"
    email_warning_xpath = "//input[@name='email']/following-sibling::div"
    password_warning_xpath = "//input[@name='password']/following-sibling::div"

    def enter_firstname_and_lastname(self,fname,lname):
        self.type_into_element("firstname_locator_name",self.firstname_locator_name,fname)
        self.type_into_element("lastname_locator_name",self.lastname_locator_name,lname)
        #self.driver.find_element(By.NAME,self.first_name_locator_name).send_keys(fname)
        #self.driver.find_element(By.NAME, self.last_name_locator_name).send_keys(lname)

    def enter_email(self,email):
        self.type_into_element("email_field_locator_name",self.email_field_locator_name,email)
        #self.driver.find_element(By.NAME, self.email_field_locator_name).send_keys(email)

    def enter_telephone(self, telephone):
        self.type_into_element("telephone_field_locator_name",self.telephone_field_locator_name,telephone)
        #self.driver.find_element(By.NAME, self.telephone_field_locator_name).send_keys(telephone)

    def enter_and_confirm_password(self,first_time,second_time):
        self.type_into_element("password_field_locator_name",self.password_field_locator_name,first_time)
        self.type_into_element("confirm_password_locator_name",self.confirm_password_locator_name,second_time)
        #self.driver.find_element(By.NAME, self.password_field_locator_name).send_keys(first_time)
        #self.driver.find_element(By.NAME, self.confirm_password_locator_name).send_keys(second_time)

    def agree_to_privacy_and_policy(self):
        self.click_on_element("privacy_policy_agree_locator_name",self.privacy_policy_agree_locator_name)
        #self.driver.find_element(By.NAME,self.privacy_policy_agree_locator_name).click()

    def click_on_continue_button(self):
        self.click_on_element("continue_button_xpath",self.continue_button_xpath)
        #self.driver.find_element(By.XPATH,self.continue_button_xpath).click()
        return Accountpage(self.driver)

    def select_the_news_letter_radio_button(self,status):
        if status == "yes" or "Yes":
            self.click_on_element("newsletter_xpath_yes",self.newsletter_xpath_yes)
            #self.driver.find_element(By.XPATH,self.newsletter_xpath_yes).click()
        if status == "no" or "No":
            self.click_on_element("newsletter_xpath_no",self.newsletter_xpath_no)
            #self.driver.find_element(By.XPATH,self.newsletter_xpath_no).click()

    def verify_the_validation_for_already_registered_mail(self,exp_text):
        return self.retrieve_text("warning_msg_for_already_registered_email_xpath",self.warning_msg_for_already_registered_email_xpath).__contains__(exp_text)
        #return self.driver.find_element(By.XPATH,self.warning_msg_for_already_registered_email_xpath).text.__contains__(exp_text)

    """
        def verify_validation_for_empty_first_name(self,exp_text):
            return self.driver.find_element(By.XPATH,self.first_name_warning_xpath).text.__contains__(exp_text)

        def verify_validation_for_empty_last_name(self, exp_text):
            return self.driver.find_element(By.XPATH, self.last_name_warning_xpath).text.__contains__(exp_text)

        def verify_validation_for_empty_email(self, exp_text):
            return self.driver.find_element(By.XPATH, self.email_warning_xpath).text.__contains__(exp_text)

        def verify_validation_for_empty_telephone(self, exp_text):
            return self.driver.find_element(By.XPATH, self.telephone_warning_xpath).text.__contains__(exp_text)

        def verify_validation_for_empty_password(self, exp_text):
            return self.driver.find_element(By.XPATH, self.password_warning_xpath).text.__contains__(exp_text)

        def verify_validation_for_privacy_policy(self, exp_text):
            return self.driver.find_element(By.XPATH, self.privacy_policy_warning_xpath).text.__contains__(exp_text)
    """
    def Warning_messages(self,privacyPolicyWarning,firstnamevalidation,lastnamevalidation,emailvalidation,telephonevalidation,passwordvalidation):
        first_name_status = self.retrieve_text("firstname_warning_xpath",self.firstname_warning_xpath).__contains__(firstnamevalidation)
        print(first_name_status)
        last_name_status = self.retrieve_text("lastname_warning_xpath",self.lastname_warning_xpath).__contains__(lastnamevalidation)
        print(last_name_status)
        email_status = self.retrieve_text("email_warning_xpath",self.email_warning_xpath).__contains__(emailvalidation)
        print(email_status)
        telephone_status = self.retrieve_text("telephone_warning_xpath",self.telephone_warning_xpath).__contains__(telephonevalidation)
        print(telephone_status)
        password_status = self.retrieve_text("password_warning_xpath",self.password_warning_xpath).__contains__(passwordvalidation)
        print(password_status)
        privacy_status = self.retrieve_text("privacy_policy_warning_xpath",self.privacy_policy_warning_xpath).__contains__(privacyPolicyWarning)
        print(privacy_status)
        if first_name_status and last_name_status and email_status and telephone_status and password_status and privacy_status:
            return True
        else:
            return False



