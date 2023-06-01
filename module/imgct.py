import urllib.request

#===========이미지추출=========
def imgID(list_imgsrcs,filename):
    print('이미지 추출 중.....')

    count = 1


    for list_imgsrc in list_imgsrcs:
        urllib.request.urlretrieve(list_imgsrc, './img/{0}/'.format(filename) + "{0}.jpg".format(count))
        count += 1


    print('추출 끝')




