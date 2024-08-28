from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I got navigated to home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/index.php?")

@when(u'I enter valid product into search box field')
def step_impl(context):#parameterizing the steps
    context.driver.find_element(By.NAME,"search").send_keys("Hp")

@when(u'I click on search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//div[@id='search']//button").click()

@then(u'valid product should be displayed in the search results')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    context.driver.quit()

@when(u'I enter Invalid product into search box field')
def step_impl(context):
    context.driver.find_element(By.NAME, "search").send_keys("Honda")

@then(u'proper error message should be displayed in the search results page')
def step_impl(context):
    exp_text="There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__contains__(exp_text)
    context.driver.quit()
@when(u'I dont enter any product into search box field')
def step_impl(context):
    context.driver.find_element(By.NAME,"search").send_keys("")