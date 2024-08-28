import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

@given(u'I should navigate to register page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/index.php?")
    context.driver.find_element(By.LINK_TEXT, "My Account").click()
    context.driver.find_element(By.LINK_TEXT, "Register").click()

@when(u'I enter details into mandatory fields')
def step_impl(context):
    context.driver.find_element(By.NAME,"firstname").send_keys("Madhu Kumar")
    context.driver.find_element(By.NAME,"lastname").send_keys("HM")
    context.driver.find_element(By.NAME,"email").send_keys("maddd.com@gmail.com")
    context.driver.find_element(By.NAME,"telephone").send_keys("8296790418")
    context.driver.find_element(By.NAME,"password").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "confirm").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "agree").click()

@when(u'Click on continue button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    time.sleep(3)

@then(u'Account should get created')
def step_impl(context):
    Exp_msg = "Your Account Has Been Created!"
    assert context.driver.find_element(By.XPATH,"//div[@id='content']/child::h1").text.__eq__(Exp_msg),"account creation failed try again"


@when(u'I enter details into All fields')
def step_impl(context):
    context.driver.find_element(By.NAME,"firstname").send_keys("Madhu Kumar")
    context.driver.find_element(By.NAME,"lastname").send_keys("HM")
    context.driver.find_element(By.NAME,"email").send_keys("madharshew.com@gmail.com")
    context.driver.find_element(By.NAME,"telephone").send_keys("8296790418")
    context.driver.find_element(By.NAME,"password").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "confirm").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.XPATH,"//label[normalize-space()='Yes']").click()

@when(u'I enter details into All fields except email field')
def step_impl(context):
    context.driver.find_element(By.NAME, "firstname").send_keys("Madhu Kumar")
    context.driver.find_element(By.NAME, "lastname").send_keys("HM")
    context.driver.find_element(By.NAME, "telephone").send_keys("8296790418")
    context.driver.find_element(By.NAME, "password").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "confirm").send_keys("Maddy@1234")
    context.driver.find_element(By.NAME, "agree").click()
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()

@when(u'I enter existing email into email field')
def step_impl(context):
    context.driver.find_element(By.NAME, "email").send_keys("madhukumarhm605@gmail.com")


@then(u'proper warning message for already register mail should be displayed')
def step_impl(context):
    warn_msg = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH,"(//div[@id='account-register']/child::div)[1]").text.__contains__(warn_msg),"registered with already registered mail"


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.driver.find_element(By.NAME, "firstname").send_keys("")
    context.driver.find_element(By.NAME, "lastname").send_keys("")
    context.driver.find_element(By.NAME, "email").send_keys("")
    context.driver.find_element(By.NAME, "telephone").send_keys("")
    context.driver.find_element(By.NAME, "password").send_keys("")
    context.driver.find_element(By.NAME, "confirm").send_keys("")
    context.driver.find_element(By.XPATH, "//label[normalize-space()='Yes']").click()

@then(u'proper warning message for every mandatory field should be displayed')
def step_impl(context):
    privacyPolicyWarning = "Warning: You must agree to the Privacy Policy!"
    firstNameValidation = "First Name must be between 1 and 32 characters!"
    lastNameValidation = "Last Name must be between 1 and 32 characters!"
    emailValidation = "E-Mail Address does not appear to be valid!"
    telephoneValidation = "Telephone must be between 3 and 32 characters!"
    passwordValidation = "Password must be between 4 and 20 characters!"
    assert context.driver.find_element(By.XPATH,"(//ul[@class='breadcrumb']/following-sibling::div)[1]").text.__contains__(privacyPolicyWarning)
    assert context.driver.find_element(By.XPATH,"//input[@name='firstname']/following-sibling::div").text.__contains__(firstNameValidation),"first name is filled"
    assert context.driver.find_element(By.XPATH,"//input[@name='lastname']/following-sibling::div").text.__contains__(lastNameValidation),"last name is filled"
    assert context.driver.find_element(By.XPATH,"//input[@name='email']/following-sibling::div").text.__contains__(emailValidation),"email is filled"
    assert context.driver.find_element(By.XPATH,"//input[@name='telephone']/following-sibling::div").text.__contains__(telephoneValidation),"telephone number is filled"
    assert context.driver.find_element(By.XPATH,"//input[@name='password']/following-sibling::div").text.__contains__(passwordValidation),"password is entered is filled"
