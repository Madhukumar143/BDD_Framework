from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I navigate to the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/index.php?")
    context.driver.find_element(By.LINK_TEXT, "My Account").click()
    context.driver.find_element(By.LINK_TEXT, "Login").click()


@when(u'i enter user name as "{Username}" and password as "{Password}" into the fields')
def step_impl(context, Username, Password):
    context.driver.find_element(By.NAME, "email").send_keys(Username)
    context.driver.find_element(By.NAME, "password").send_keys(Password)


@when(u'I click on Login button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//input[@value='Login']").click()

@then(u'I should be successfully logged in')
def step_impl(context):
    assert context.driver.find_element(By.LINK_TEXT,"Edit your account information").is_displayed(),"login failed with valid credentials please try again"

@when(u'i enter valid Email and invalid Password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, "email").send_keys("madhukumarhm605@gmail.com")
    context.driver.find_element(By.NAME, "password").send_keys("Password")

@then(u'I should get a proper warning message')
def step_impl(context):
    exp_msg= "Warning: No match for E-Mail Address and/or Password."
    assert context.driver.find_element(By.XPATH,"//div[@id='account-login']/div[1]").text.__contains__(exp_msg)

@when(u'i enter Invalid Email and Valid Password into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, "email").send_keys("madhukumarhm600@gmail.com")
    context.driver.find_element(By.NAME, "password").send_keys("Madhu@1234")
