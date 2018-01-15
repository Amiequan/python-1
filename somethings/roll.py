#encoding=utf-8
from selenium import webdriver
import time

"""滚动条操作"""

driver=webdriver.Chrome(executable_path="c:\\Python36\\chromedriver")
driver.get("http://blog.sina.com.cn/#")
time.sleep(2)
#滚动到最下方
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
#滚动到最上方
driver.execute_script("window.scrollTo(0, 0);")
time.sleep(2)
#滚动到指定位置
driver.execute_script("window.scrollTo(0, 2500);")
time.sleep(2)
#滚动到最上方
driver.execute_script("window.scrollTo(document.body.scrollWidth, 0);")