from selenium import webdriver

driver = webdriver.Chrome('./chromedriver.exe')
driver.get(url='https://www.google.com/')

driver.quit()
