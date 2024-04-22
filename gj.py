from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 启用带用户数据配置的浏览器
option = webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
option.add_argument("--user-data-dir="+r"D:\webbro\3")
chrome_options = Options()
driver = webdriver.Chrome(option)   # 打开chrome浏览器
driver.get('https://xion.bonusblock.io/')
# driver.find_element(By.ID,'kw').send_keys('python')
# driver.find_element(By.ID,'su').click()
driver.find_element(By.XPATH,'//*[@id="app"]/section/main/div[2]/div/div/div[3]').click()


driver.find_element(By.XPATH,'//*[@id="radix-:r0:"]/div/div[2]').send_keys('454711920@qq.com')
#下面写其他操作
