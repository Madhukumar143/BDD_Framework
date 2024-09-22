from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class BasePage:

    def __init__(self,driver):
        self.driver = driver

    def click_on_element(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        element.click()
    def type_into_element(self,locator_type,locator_value,text_to_enter):
        element = self.get_element(locator_type,locator_value)
        element.clear()
        element.send_keys(text_to_enter)

    def  check_display_status(self,locator_type,locator_value):
        element = self.get_element(locator_type,locator_value)
        return element.is_displayed()

    def retrieve_text(self, locator_type, locator_value):
        element = self.get_element(locator_type,locator_value)
        return element.text


    def get_element(self,locator_type,locator_value):
        element = None
        try:
            if locator_type.__contains__("_id"):
                element = self.driver.find_element(By.ID, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_type.__contains__("_name"):
                element = self.driver.find_element(By.NAME, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_type.__contains__("_xpath"):
                element = self.driver.find_element(By.XPATH, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_type.__contains__("linktext"):
                element = self.driver.find_element(By.LINK_TEXT, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_type.__contains__("_class_name"):
                element = self.driver.find_element(By.CLASS_NAME, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
            elif locator_type.__contains__("_css"):
                element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
                if element.is_displayed():
                    return element
                else:
                    return False
        except NoSuchElementException:
            return False