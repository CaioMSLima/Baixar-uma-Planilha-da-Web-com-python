from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://br.investing.com/currencies/usd-brl-historical-data')


time.sleep(5)
driver.find_elements_by_id("onetrust-accept-btn-handler")[0].click()

time.sleep(5)
driver.find_elements_by_xpath(
    '//*[@id="PromoteSignUpPopUp"]/div[2]/i')[0].click()

time.sleep(5)
driver.find_elements_by_xpath(
    '//*[@id="column-content"]/div[4]/div/a')[0].click()

time.sleep(5)
email = input('Digite seu email')
senha = input('Digite a senha')
driver.find_element_by_name('loginFormUser_email').send_keys(email)
driver.find_element_by_id('loginForm_password').send_keys(senha)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="signup"]/a').click()

time.sleep(3)
driver.find_elements_by_xpath(
    '//*[@id="column-content"]/div[4]/div/a')[0].click()
