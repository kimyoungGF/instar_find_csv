from selenium.webdriver.common.keys import Keys
import time
import os
from os import path
from selenium.webdriver.common.by import By
from module.imgct import imgID


#============들어가기========
def inID(driver,list_bestids):

    for i in range(0,len(list_bestids)-1):

        time.sleep(8)
        driver.get('{0}'.format(list_bestids[i]))

        time.sleep(8)


        #===========================================

        driver.find_element(By.CLASS_NAME,"_aap6._aap7._aap8").click()
        time.sleep(8)


        # ============파일생성===========
        bestidname = driver.find_elements(By.CLASS_NAME,"_aacl._aacs._aact._aacx._aada")

        filename = bestidname[0].text

        if not path.isdir('./img/{0}/'.format(filename)):
            os.mkdir('./img/{0}/'.format(filename))
            print('{0} 생성'.format(filename))




        #id화면으로 이동

        time.sleep(5)

        imgsrc=set()

        p = driver.find_element(By.CSS_SELECTOR,'body')

        #=====src추출 함수=====

        imgcountb=0
        imgcountf=1

        while imgcountb < imgcountf:

            imgcountb = len(imgsrc)

            k = driver.find_elements(By.CLASS_NAME,'_aagt')

            for uurl in k:
                imgsrc.add(uurl.get_attribute('src'))
            p.send_keys(Keys.PAGE_DOWN)
            time.sleep(8)

            imgcountf = len(imgsrc)

        print('지금까지 수집한 이미지의 src 총 개수 : ', len(imgsrc))

        list_imgsrcs = list(imgsrc)#set list화

        time.sleep(3)

        imgID(list_imgsrcs,filename)

        time.sleep(3)



