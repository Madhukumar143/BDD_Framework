from selenium.webdriver.common.by import By

from features.Pages.Basepage import BasePage
from features.Pages.Loginpage import LoginPage
from features.Pages.Registerpage import Registerpage


class Homepage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    my_account_option_linktext = "My Account"
    login_option_linktext = "Login"
    search_box_name = "search"
    search_button_xpath = "//div[@id='search']//button"
    searched_element_xpath = "//a[normalize-space()='HP LP3065']"
    invalid_searched_result_xpath = "//input[@id='button-search']/following-sibling::p"
    register_option_linktext = "Register"

    def click_on_my_account(self):
        self.click_on_element("my_account_option_linktext",self.my_account_option_linktext)
        #self.driver.find_element(By.LINK_TEXT,self.my_account_option_linkText).click()

    def click_on_Login_option(self):
        self.click_on_element("login_option_linktext",self.login_option_linktext)
        #self.driver.find_element(By.LINK_TEXT,self.login_option_linktext).click()
        return LoginPage(self.driver)

    def click_on_register_option(self):
        self.click_on_element("register_option_linktext",self.register_option_linktext)
        #self.driver.find_element(By.LINK_TEXT,self.register_option_linktext).click()
        return Registerpage(self.driver)

    def check_homepage_title(self,exp_title):
        return self.driver.title.__eq__(exp_title)

    def enter_product_into_search_box(self,product_text):
        self.type_into_element("search_box_name",self.search_box_name,product_text)
        #self.driver.find_element(By.NAME,self.search_box_name).send_keys(product_text)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath",self.search_button_xpath)
        #self.driver.find_element(By.XPATH,self.search_button_xpath).click()


    def display_status_of_searched_element(self):
        return self .check_display_status("searched_element_xpath",self.searched_element_xpath)
        #return self.driver.find_element(By.XPATH,self.searched_element_xpath).is_displayed()

    def verify_the_result_for_invalid_search(self,exp_text):
        return self.retrieve_text("invalid_searched_result_xpath",self.invalid_searched_result_xpath).__contains__(exp_text)
        #return self.driver.find_element(By.XPATH,self.invalid_searched_result_xpath).text.__contains__(exp_text)
