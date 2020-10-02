print('Введите е-мэйл или номер телефона')
eml=str(input())

print('Введите пароль')
paswd=str(input())

import time

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://vk.com/")

email = driver.find_element_by_css_selector("#index_email")
email.send_keys(eml)

password = driver.find_element_by_css_selector("#index_pass")
password.send_keys(paswd)

submit_button = driver.find_element_by_css_selector("#index_login_button")
submit_button.click()

friends_button = driver.find_element_by_css_selector("#l_fr")
friends_button.click()
