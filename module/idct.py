from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import csv
import datetime as dt



def idcollect(driver):
    d = dt.datetime.now()
    day=d.strftime("%m_%d_%H_%M")

    #--------주소 수집--------

    print('href를 수집합니다.')

    bestid = set() #주소 href

    k = driver.find_elements(By.CLASS_NAME,'oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._a6hd')



    countbestid=0


    j = driver.find_element(By.CSS_SELECTOR, 'body')

    while countbestid < 30:

        k = driver.find_elements(By.CLASS_NAME,'oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl._a6hd')
        time.sleep(5)


        for idnum in range(0,30):
            bestid.add(k[idnum].get_attribute('href'))


        countbestid=len(bestid)

        j.send_keys(Keys.PAGE_DOWN)
        print(len(bestid))
        time.sleep(5)


    list_bestids = list(bestid)

    with open("./instarset({0}).csv".format(day), 'w') as file:
        writer = csv.writer(file)
        writer.writerow(list_bestids)


    print('총 {0}명의 href를 수집하였습니다.'.format(len(list_bestids)))

    return list_bestids
