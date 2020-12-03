from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request

#=========================================이미지 저장해주는 코드============================================
# driver = webdriver.Chrome() #크롬 브라우저를 킨다
# driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ogbl") #크롬브라우저 이미지검색 url로 접속을 한다
# elem = driver.find_element_by_name("q") #elem이란 변수에 q라는 이름을 가진(검색창)을 넣어준다.
# elem.send_keys("비트코인") #그 키에 ''안에 찾고싶은 것을 넣어준다  정확한 명령어를 모를 땐 검색하기 ex) python selenium key press 파이썬 셀레니움 키 입력
# elem.send_keys(Keys.RETURN) # enter
# images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")
# count = 1
# for image in images:
#     try:
#         image.click()
#         time.sleep(2)
#         imgurl = driver.find_element_by_css_selector(".n3VNCb").get_attribute("src")
#         urllib.request.urlretrieve(imgurl, 'image/' + str(count) + '.jpg')
#         count = count + 1
#     except:
#         pass
# driver.close()

# =============================페이스북 들어가는 python코드 =========================================
# pass1 = str("5855mj!!")
# email= "01063359627"
# driver = webdriver.Chrome()
# driver.get("http://www.facebook.com")
# time.sleep(1)
# element = driver.find_element_by_id("email")
# element.send_keys(email,Keys.TAB) #키보드를 사용할 수 있게끔 만드는
# time.sleep(1)
# element_pwd = driver.find_element_by_id("pass")
# element_pwd.send_keys(pass1) #키보드를 사용할 수 있게끔 만드는
# element.submit()

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/")

imgurl = driver.find_element_by_id("img").get_attribute("src")
urllib.request.urlretrieve(imgurl, 'image/' + '11' + '.jpg')
