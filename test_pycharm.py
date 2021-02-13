import numpy as np
import pandas as pd
import re
import selenium
from selenium import webdriver
import time
driver = webdriver.Safari()
driver.get("https://www.zillow.com/homes/newyork_rb/")

page_index=1
item_scraped=0

t_price=[]
t_bedrooms=[]
t_bathrooms=[]
t_area=[]
t_item_type=[]
t_address=[]
t_item_link=[]

t_zelle_estimate_month=[]
t_construction=[]
t_heating=[]
t_cooling=[]
t_garage=[]
t_hoa=[]
t_lot=[]
t_price_area=[]

while page_index<=1 :

    print("currently on" +str(page_index))
    items = driver.find_elements_by_xpath('//ul[@class="photo-cards photo-cards_wow photo-cards_short photo-cards_extra-attribution"]/li')
    counter=0

    for index,item in enumerate(items):

            try:
                price = item.find_element_by_xpath('.//div[@class="list-card-price"]').text
                price = float(price.replace(',','').replace('$',''))
                t_price.extend([price])
            except:
                continue
            try :
                bedrooms  = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[1]').text
                bedrooms  = float(re.findall('\d{1,}\.{0,1}\d{0,1}',bedrooms)[0])
                t_bedrooms.extend([bedrooms])
            except :
                bedrooms = bedrooms
            try:
                bathrooms = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[2]').text
                bathrooms = float(re.findall('\d{1,}\.{0,1}\d{0,1}',bathrooms)[0])
                t_bathrooms.extend([bathrooms])
            except:
                bathrooms = 'NA'
            try:
                area = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[3]').text
                area = area.replace(',','')
                area = float(re.findall('\d{1,}\d{0,1}',area)[0])
                t_area.extend([area])
            except:
                area ='NA'
            try:
                item_type = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[4]').text
                item_type = item_type.strip().replace('-',' ').strip()
                t_item_type.extend([item_type])
            except :
                item_type='NA'
            try:
                address = item.find_element_by_xpath('.//address[@class="list-card-addr"]').text
                t_address.extend([address])
            except:
                address='NA'
            try:
                item_link = item.find_element_by_xpath('.//a[@class="list-card-link list-card-link-top-margin"]')
                item_link = item_link.get_attribute("href")
                t_item_link.extend([item_link])
                counter+=1
            except:
                item_link='NA'
                t_item_link.extend([item_link])
                counter+=1

    driver.quit()
    for sub_item in range(item_scraped,item_scraped+counter):

        try:
            driver.get(t_item_link[sub_item])
        except:
            t_zelle_estimate_month.extend(['NA'])
            t_construction.extend(['NA'])
            t_heating.extend(['NA'])
            t_cooling.extend(['NA'])
            t_garage.extend(['NA'])
            t_hoa.extend(['NA'])
            t_lot.extend(['NA'])
            continue

        try:
            z_estimate=driver.find_element_by_xpath('.//div[@class="sc-fzpans cKJzHK"]/span[2]').text
            z_estimate=re.findall('\d{1,}\,{0,1}\d{0,}',z_estimate)[0]
            z_estimate=z_estimate.replace(',','')
            t_zelle_estimate_month.extend([z_estimate])
        except:
            t_zelle_estimate_month.extend(['NA'])

        try:
            facts_feature_button=driver.find_element_by_xpath('.//a[@class="hdp__mg5mjz-5 jgIHSZ active"]')
            facts_feature_button.click()
            construction=driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            t_construction.extend([construction])
        except:
            t_construction.extend(['NA'])

        try:
            heating=driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            t_heating.extend([heating])
        except:
            t_heating.extend(['NA'])

        try:
            cooling = driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            t_cooling.extend([heating])
        except:
            t_cooling.extend(['NA'])

        try:
            parking = driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            t_garage.extend([parking])
        except:
            t_garage.extend(['NA'])

        try:
            hoa = driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            hoa=re.findall('\d{1,}\,{0,1}\d{0,}',hoa)[0].replace(',','')
            t_hoa.extend([hoa])
        except:
            t_hoa.extend(['NA'])

        try:
            price_are = driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
            price_are = re.findall('\d{1,}\,{0,1}\d{0,}',price_are)[0].replace(',','')
            t_price_area.extend(float(price_are))
        except:
            t_price_area.extend(['NA'])

        try:
            home_value_button = driver.find_element_by_xpath('.//a[@class="hdp__mg5mjz-5 jgIHSZ active"]')
            home_value_button.click()
        except:
            



    page_index +=1
driver.quit()