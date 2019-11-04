from selenium import webdriver

driver = webdriver.Chrome('/home/ariana/Downloads/chromedriver')
driver.get('http://localhost:8000')

assert 'Django' in driver.title
