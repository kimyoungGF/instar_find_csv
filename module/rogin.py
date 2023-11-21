from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

def rogin(driver):
    # ===========로그인정보, 검색할것=========
    ID = '--
    PW = '--'
    SH = '--'

    # ===========주소입력=========
    url = 'https://www.instagram.com/'
    driver.get(url)
    driver.implicitly_wait(3)

    time.sleep(5)



    # ===========로그인과 창 뜨면 제거=========
    e = driver.find_element('name','username')
    e.clear()
    e.send_keys(ID)

    time.sleep(5)

    e = driver.find_element('name','password')
    e.clear()
    e.send_keys(PW)

    e.send_keys(Keys.ENTER)

    time.sleep(5)


    try:
        driver.find_element(By.CLASS_NAME,"cmbtv").click()
    except:
        pass

    try:
        driver.find_element(By.CLASS_NAME,"_a9--._a9_1").click()
    except:
        pass

    print("로그인 성공{0}를 검색합니다.".format(SH))
    time.sleep(3)

    # ===========검색============
    e = driver.find_element(By.CLASS_NAME,'_aauy')
    time.sleep(2)
    e.clear()
    time.sleep(2)
    e.send_keys(SH)

    time.sleep(5)

    e = driver.find_element(By.CLASS_NAME,'_abnr._abnu')
    time.sleep(2)
    e.click()

    time.sleep(5)

    #로그인 완
    print('셀카검색 완')
