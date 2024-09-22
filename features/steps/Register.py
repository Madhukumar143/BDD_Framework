import time
from datetime import datetime

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.Pages.HomePage import Homepage
from features.Pages.Registerpage import Registerpage
from features.Pages.accountsPage import Accountpage


@given(u'I should navigate to register page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    context.homepage.click_on_my_account()
    context.registerpage  = context.homepage.click_on_register_option()

@when(u'I enter details into mandatory fields')
def step_impl(context):
    time_stamp = (datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    new_email = "madhu" + time_stamp + "@gmail.com"
    context.registerpage.enter_firstname_and_lastname("Madhu kumar","HM")
    context.registerpage.enter_telephone(8296798325)
    context.registerpage.enter_email(new_email)
    context.registerpage.enter_and_confirm_password("Maddy@1234","Maddy@1234")
    context.registerpage.agree_to_privacy_and_policy()

@when(u'Click on continue button')
def step_impl(context):
    context.accountpage = context.registerpage.click_on_continue_button()

@then(u'Account should get created')
def step_impl(context):
    Exp_msg = "Your Account Has Been Created!"
    assert context.accountpage.check_status_of_account_registration(Exp_msg),"account creation failed try again"

@when(u'I enter details into All fields')
def step_impl(context):
    time_stamp = (datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))
    new_email = "madhu" + time_stamp + "@gmail.com"
    context.registerpage.enter_firstname_and_lastname("Madhu kumar", "HM")
    context.registerpage.enter_telephone(8296798325)
    context.registerpage.enter_email(new_email)
    context.registerpage.enter_and_confirm_password("Maddy@1234", "Maddy@1234")
    context.registerpage.agree_to_privacy_and_policy()
    context.registerpage.select_the_news_letter_radio_button("Yes")

@when(u'I enter details into All fields except email field')
def step_impl(context):
    context.registerpage.enter_firstname_and_lastname("Madhu kumar", "HM")
    context.registerpage.enter_telephone(8296798325)
    context.registerpage.enter_and_confirm_password("Maddy@1234", "Maddy@1234")
    context.registerpage.agree_to_privacy_and_policy()
    context.registerpage.select_the_news_letter_radio_button("Yes")

@when(u'I enter existing email into email field')
def step_impl(context):
    context.registerpage.enter_email("madhukumarhm605@gmail.com")


@then(u'proper warning message for already register mail should be displayed')
def step_impl(context):
    warn_msg = "Warning: E-Mail Address is already registered!"
    assert context.registerpage.warning_msg_for_already_registered_email_xpath,"you have registered with this email already"


@when(u'I dont enter anything into the fields')
def step_impl(context):
    context.registerpage.enter_firstname_and_lastname("","")
    context.registerpage.enter_telephone("")
    context.registerpage.enter_email("")
    context.registerpage.enter_and_confirm_password("", "")

@then(u'proper warning message for every mandatory field should be displayed')
def step_impl(context):
    privacyPolicyWarning = "Warning: You must agree to the Privacy Policy!"
    firstNameValidation = "First Name must be between 1 and 32 characters!"
    lastNameValidation = "Last Name must be between 1 and 32 characters!"
    emailValidation = "E-Mail Address does not appear to be valid!"
    telephoneValidation = "Telephone must be between 3 and 32 characters!"
    passwordValidation = "Password must be between 4 and 20 characters!"
    assert context.registerpage.Warning_messages(privacyPolicyWarning,firstNameValidation,
                                                 lastNameValidation,emailValidation,
                                                 telephoneValidation,passwordValidation),"you entered some fields"
    """assert context.registerpage.verify_validation_for_privacy_policy(privacyPolicyWarning),"you have agreed to privacy and policy"
    assert context.registerpage.verify_validation_for_empty_first_name(firstNameValidation),"first name is filled"
    assert context.registerpage.verify_validation_for_empty_last_name(lastNameValidation),"last name is filled"
    assert context.registerpage.verify_validation_for_empty_email(emailValidation),"email is filled"
    assert context.registerpage.verify_validation_for_empty_telephone(telephoneValidation),"telephone number is filled"
    assert context.registerpage.verify_validation_for_empty_password(passwordValidation),"password is entered is filled"""