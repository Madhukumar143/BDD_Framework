import allure
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context,driver):

    context.driver = webdriver.Chrome()
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))
def after_scenario(context,driver):
    screenshot = context.driver.get_screenshot_as_png()
    # Attach it to allure report
    allure.attach(screenshot, name='screenshot', attachment_type=AttachmentType.PNG)
    context.driver.quit()