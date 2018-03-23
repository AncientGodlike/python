from selenium import webdriver
import time
import pickle

url = 'http://passport.zhihuishu.com/login'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(5)


with open('data.txt','rb') as file:
	b = pickle.load(file)

#定位输入账号地方
username = driver.find_element_by_id('lUsername')
username.clear()
#填写账号
username.send_keys(b['account'])
password = driver.find_element_by_id('lPassword')
password.clear()
password.send_keys(b['key'])
#点击登陆按钮
driver.find_element_by_xpath('.//span[@class="wall-sub-btn"]').click()



