from selenium import webdriver
from module.rogin import rogin
from module.idct import idcollect
from module.intoid import inID


#===========크롬드라이버=========
chrome = 'c:/temp/chromedriver.exe'


driver = webdriver.Chrome(chrome)

rogin(driver)

list_bestids = idcollect(driver)

inID(driver,list_bestids)






