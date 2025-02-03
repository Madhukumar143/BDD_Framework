from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.HomePage import Homepage
from features.Pages.Loginpage import LoginPage
from features.Pages.accountsPage import Accountpage

@given(u'I navigate to the login page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.homepage.click_on_my_account()
    context.loginpage = context.homepage.click_on_Login_option()

@when(u'i enter user name as "{email}" and password as "{password}" into the fields')
def step_impl(context,email,password):
    context.loginpage.enter_email_adress(email)
    context.loginpage.enter_the_password(password)

@when(u'I click on Login button')
def step_impl(context):
    context.accountpage = context.loginpage.click_on_login_button()

@then(u'I should be successfully logged in')
def step_impl(context):
    assert context.accountpage.display_status_of_edit_account(),"login failed with valid credentials please try again"

@when(u'i enter valid Email as "{email}" and invalid Password as "{password}" into the fields')
def step_impl(context,email,password):
    context.loginpage.enter_email_adress(email)
    context.loginpage.enter_the_password(password)

@then(u'I should get a proper warning message')
def step_impl(context):
    exp_msg= "Warning: No match for E-Mail Address and/or Password."
    assert context.loginpage.display_status_of_warning_message(exp_msg),"failed logged in with invalid credentials"

@when(u'i enter Invalid Email and Valid Password as "{password}" into the fields')
def step_impl(context,password):
    time_stamp = (datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    invalid_email = "madhu" + time_stamp + "@gmail.com"
    context.loginpage.enter_email_adress(invalid_email)
    context.loginpage.enter_the_password(password)
