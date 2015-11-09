#encoding=utf-8
"""此代码于本地环境运行，拉起浏览器模拟人工操作获取所需数据，每次运行需人工更改存放有url的txt文件文件名以及生成json文件文件名
"""
import json
import time
from selenium import webdriver

driver = webdriver.Firefox()

textpath=r"2015-10-14-10-20.txt"                                       #存放的url文本路径
text=open(textpath)
arr=[]
for lines in text.readlines():
    lines=lines.replace("\n","")
    arr.append(lines)
text.close()

sName = '2015-10-14-10-20.json'                                        #所需写入json文件文件名
f = open(sName,'w+')
for url in arr:
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_partial_link_text(u'工具').click()           #模拟点击操作
    try:
        result = driver.find_element_by_id('resultStats').text
    except:
        time.sleep(1)                                                  #模拟点击获取数据失败后再次尝试
        driver.find_element_by_partial_link_text(u'工具').click()
        result = driver.find_element_by_id('resultStats').text
    keyword = driver.title
    data = {}
    data["keyword"] = keyword
    data["result"] = result

    jsonStr = json.dumps(data)
    f.write(jsonStr)
    f.write('\n')
driver.quit()
f.close