##
import os
from selenium import webdriver
import json
import time

xpthDse='/html/body/div[2]/section/div/div[1]/div/div[1]/div[4]'
xpthDse2='/html/body/div[2]/section/div/div[1]/div/div[1]/div[2]'
xpthCse='//*[@id="lblIndexChp1"]'
xpthCse2='//*[@id="lblIndex1"]'
xpthXe='//*[@id="converterResult"]/div/div/div[2]/span[1]'
xpthKitcoBid='//*[@id="sp-bid"]'
xpthKitcoChng='//*[@id="sp-chg-percent"]'
xpthBitkub='//*[@id="main"]/div[3]/div[2]/div/a[1]/div/div[1]/div[2]/span'
xpthBitkub2='//*[@id="main"]/div[3]/div[2]/div/a[1]/div/div[1]/div[3]/span'
op=webdriver.ChromeOptions()
op.add_argument('headless')
urlDse='http://dsebd.org/'
urlCse='https://www.berichbd.com/'
urlXe='https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=SGD'
urlKitco='https://www.kitco.com/charts/livegold.html'
urlBitkub='https://www.bitkub.com'
while True:
    driver = webdriver.Chrome(options=op)
    driver1 = webdriver.Chrome(options=op)
    driver1.get(urlBitkub)

    driver.get(urlDse)
    # time.sleep(5)
    DSE1 = driver.find_element_by_xpath(xpthDse).text
    DSE2 = driver.find_element_by_xpath(xpthDse2).text
    #print(DSE1)
    #print(DSE2)

    driver.get(urlCse)
    CSE1 = driver.find_element_by_xpath(xpthCse2).text
    CSE2 = driver.find_element_by_xpath(xpthCse).text
    #print(CSE2)
    #print(CSE1)

    driver.get(urlXe)
    SGD = driver.find_element_by_xpath(xpthXe).text
    #print(SGD)

    driver.get(urlKitco)
    GOLD1 = driver.find_element_by_xpath(xpthKitcoBid).text
    GOLD2 = driver.find_element_by_xpath(xpthKitcoChng).text
    #print(GOLD1)
    #print(GOLD2)
    BTC1 = driver1.find_element_by_xpath(xpthBitkub).text
    BTC2 = driver1.find_element_by_xpath(xpthBitkub2).text
    #print(BTC1)
    #print(BTC2)
    driver.close()
    driver1.close()
    dictionary = [{
        'CSE': CSE1,
        'DSE': DSE2,
        'GOLD': GOLD1,
        'BITCOIN': BTC1,
        'SGD': SGD
    }, {
        'CSE': CSE2,
        'DSE': DSE1,
        'GOLD': GOLD2,
        'BITCOIN': BTC2,
        'SGD': ''
    }]

    json_object = json.dumps(dictionary, indent=2)

    # Writing to sample.json
    with open("demo.json", "w") as outfile:
        outfile.write(json_object)

    time.sleep(180)
