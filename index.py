from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import urllib.request

#=========================================이미지 저장해주는 코드============================================
driver = webdriver.Chrome() #크롬 브라우저를 킨다
driver.get("http://www.youth.go.kr/youth/act/actSearch/allActSearchLst.yt?sCrtfcText=&sSttemntText=&sort=&order=&page=1&rows=&kCrtfcSn=&kFcltySn=&kSnOne=&kProgrmseCode=&kSnTwo=&kSttemntManageNo=&kSttemntSn=&kCrtfcAt=&kSttemntAt=&kSttemntNo=&kExclnccrtfcAtchmnflId=&searchDtl=&search=&sActRelmcode=&sActRelmcode1=&sActRelmcode2=&sActRelmcode3=&sActRelmcode4=&sActRelmcode5=&sActRelmcode6=&sActRelmcode7=&sActRelmcode8=&sActRelmcode9=&sActRelmcode10=&sActRelmcode11=&sActRelmcode12=&nas.cmm.token.html.TOKEN=17b89c3ec71facaa8dd1f669f4693e7f&sKeyword=&sActCtprvnCode1=&sActSignguCode1=&sActCtprvnCode2=&sActSignguCode2=&sActCtprvnCode3=&sActSignguCode3=&sInsttTyCode=&sInsttTyCode2=&sTrget=&sAge=&stayng=&pc=&acteraDe=thtiMt&sActeraBeginDe=2020-12-01&sActeraEndDe=2020-12-31&sCurSearchFlag=Y&sChkSearchFlag=Y") #크롬브라우저 이미지검색 url로 접속을 한다
# elem = driver.find_element_by_css_selector("ul.actlist-thum-ul") #elem이란 변수에 q라는 이름을 가진(검색창)을 넣어준다.
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
time.sleep(3)
driver.find_element_by_css_selector(".act-name-box a:first-child").click()
driver.close()

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

# driver = webdriver.Chrome()
# driver.get("https://www.youtube.com/")

# imgurl = driver.find_element_by_id("img").get_attribute("src")
# urllib.request.urlretrieve(imgurl, 'image/' + '11' + '.jpg')
