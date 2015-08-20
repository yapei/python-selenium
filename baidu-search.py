#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#访问百度
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
time.sleep(3)

#搜索
#driver.find_element_by_id("kw").send_keys("selenium") 
#driver.find_element_by_id("su").click()
#time.sleep(3)

#将页面滚动条拖到底部
#js="var q=document.documentElement.scrollTop=10000"
#driver.execute_script(js)
#time.sleep(3)


#将滚动条移动到页面的顶部
#js="var q=document.documentElement.scrollTop=0"
#driver.execute_script(js)
#time.sleep(3)

# 设置-> 搜索设置
#driver.find_element_by_link_text("设置").click()
#driver.find_element_by_link_text("搜索设置").click()
#driver.find_element_by_xpath("//span[@title='关闭']").click()

# 回到百度首页
#driver.find_element_by_xpath("//a[@class='toindex']").click()
#time.sleep(3)

#登录
#driver.find_element_by_name("tj_login").click()
#driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys("peiyadan")
#driver.find_element_by_id("TANGRAM__PSP_8__userName").send_keys(Keys.TAB)
#driver.find_element_by_id("TANGRAM__PSP_8__password").send_keys("Baidu@123!")
#time.sleep(3)
#driver.find_element_by_id("TANGRAM__PSP_2_closeBtn").click()

#更多产品
#driver.find_element_by_name("tj_briicon").click()
#driver.find_element_by_name("tj_zhidao").click()
#time.sleep(5)

# 首页图片
driver.find_element_by_xpath("//img[@src='//www.baidu.com/img/270jijian_08e16a020accb243ae867511145d916c.png']").click()
time.sleep(4)

driver.quit()
