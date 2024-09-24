from behave import *
from features.Pages.HomePage import Homepage

@given(u'I got navigated to home page')
def step_impl(context):
    context.homepage = Homepage(context.driver)
    assert context.homepage.check_homepage_title("Your Store"),"title did not match"

@when(u'I enter valid product say "{product_name}" into search box field')
def step_impl(context,product_name):
    context.homepage.enter_product_into_search_box(product_name)

@when(u'I click on search button')
def step_impl(context):
    context.homepage.click_on_search_button()

@then(u'valid product should be displayed in the search results')
def step_impl(context):
    assert context.homepage.display_status_of_searched_element(),"element not found"

@when(u'I enter Invalid product say "{product_name}" into search box field')
def step_impl(context,product_name):
    context.homepage.enter_product_into_search_box(product_name)

@then(u'proper error message should be displayed in the search results page')
def step_impl(context):
    exp_text="There is no product that matches the search criteria."
    assert context.homepage.verify_the_result_for_invalid_search(exp_text),"results found for invalid search"

@when(u'I dont enter any product into search box field')
def step_impl(context):
    context.homepage.enter_product_into_search_box("")