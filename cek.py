from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import json

sayfasayisi=100
sayfailansayisi=24
driver = webdriver.Chrome()

driver.get('https://www.sahibinden.com/kategori/otomobil')
f = open('sahibinden-araba.txt', 'w', encoding='utf8')

for x in range(1, 50):
    driver.get('https://www.sahibinden.com/vasita?pagingOffset='+str(x)+'#/')
    for y in range(1, 15):
        driver.implicitly_wait(3)
        a = driver.find_elements_by_css_selector('.search-result-item > a')[y].click()
        if a == '':
            continue
        else:
            a
        isim = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[2]/div/div[1]/div/div[1]/div/h1/div')
        if isim == None:
            continue
        else:
            isim
        driver.implicitly_wait(2)
        telno = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div[1]/div/div[1]/a[2]')
        if telno == None:
            continue
        else:
            telno
        data = []
        y = {'isim' : 'isim', 'tel no' : telno.text}
        data.append(y)

        z = json.dumps(data, indent = 4)
        f.write(z)
        print(y)
        driver.back()

        # css selector -> driver.find_element_by_class('grid')