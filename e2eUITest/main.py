from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver as Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions


BASE_URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'


def create_driver():
    options = ChromeOptions()
    driver = Chrome(options=options)

    return driver


def test_login(driver, url):
    try:
        driver.get(url)
        login_input = driver.find_element(by=By.ID, value='user-name')
        password = driver.find_element(by=By.ID, value='password')
        login_input.send_keys(LOGIN)
        password.send_keys(PASSWORD)
        button = driver.find_element(by=By.ID, value='login-button')
        button.click()

    except Exception as exp:
        print('Error authorization: ', exp)


def choose_item_and_add_to_cart(driver):
    try:
        button = driver.find_element(by=By.ID, value='add-to-cart-sauce-labs-backpack')
        button.click()

    except NoSuchElementException as ex:
        print(ex)


def making_a_purchase(driver):
    try:
        cart = driver.find_element(by=By.CLASS_NAME, value='shopping_cart_link')
        cart.click()
        try:
            driver.find_element(by=By.CLASS_NAME, value='cart_item')
        except NoSuchElementException as ex:
            print('Item is not found at cart! ', ex)
        button = driver.find_element(by=By.ID, value='checkout')
        button.click()
        first_name = driver.find_element(by=By.ID, value='first-name')
        first_name.send_keys('Дмитрий')
        last_name = driver.find_element(by=By.ID, value='last-name')
        last_name.send_keys('Прокофьев')
        postal_code = driver.find_element(by=By.ID, value='postal-code')
        postal_code.send_keys('1111')
        button = driver.find_element(by=By.ID, value='continue')
        button.click()
        finish_button = driver.find_element(by=By.ID, value='finish')
        finish_button.click()
        try:
            complete = driver.find_element(by=By.CLASS_NAME, value='complete-header')
            print(complete.text)
        except NoSuchElementException as ex:
            print('The order is not been completed', ex)

    except Exception as exp:
        print(exp)

    finally:
        driver.close()
        driver.quit()


if __name__ == '__main__':
    driver = create_driver()
    test_login(driver, BASE_URL)
    choose_item_and_add_to_cart(driver)
    making_a_purchase(driver)


