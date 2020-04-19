from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

sayfasayisi=100
sayfailansayisi=24

f = open('sektordiger5.txt', 'w', encoding='utf8')
driver = webdriver.Chrome()
for x in range(85, 119):
    driver.get('https://www.sektor.gen.tr/list/diger/'+str(x))
    for y in range(1, 20):
        a = driver.find_elements_by_class_name('main-link')[y].click()
        if a == '':
            continue
        else:
            a
        isim = driver.find_element_by_class_name('subtitle')
        telno = driver.find_element_by_class_name('phone')
        if telno == '':
            continue
        else:
            telno
        data = []
        y = {'isim' : isim.text, 'tel no' : telno.text}
        data.append(y)

        z = json.dumps(data, indent = 4)
        f.write(z)
        print(y)
        driver.back()

# print(elem1.text)
# f = open('deneme1.txt', 'w', encoding='utf8')
# for i in range(1, sayfasayisi):
#     driver.get('https://www.hurriyetemlak.com/kiralik/dukkan-magaza?page='+str(i))
#     for x in range(1, sayfailansayisi):
#         driver.find_elements_by_class_name('telephone-button')[x].click()
#         elem1 = driver.find_element_by_partial_link_text('tel:')
#         driver.implicitly_wait(3)
#         print(elem1.get_attribute('href'))