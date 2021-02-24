import numpy as np
import pandas as pd
import re
import selenium
from selenium import webdriver
import time

page_index=1
item_scraped=0

t_price=[]
t_bedrooms=[]
t_bathrooms=[]
t_area=[]
t_item_type=[]
t_address=[]
t_item_link=[]

t_type=[] #done
t_construction=[]#done
t_heating=[]#done
t_cooling=[]#done
t_parking=[]#done
t_HOA=[]
t_p_s=[]
t_p_i=[]
t_mortgage=[]
t_tax=[]
t_insurance=[]
t_school=[]
t_school_ranking=[]

d={'Price':[],'Bedrooms':[],'Bathrooms':[],'Area':[],'Type':[],'Address':[],'link':[]}

while page_index<=20 :

    print("currently on" +str(page_index)+'\n')
    driver = webdriver.Safari()
    time.sleep(5)
    driver.get('https://www.zillow.com/homes/New-York,-NY_rb/'+str(page_index)+'_p/')
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
                t_bedrooms.extend([bedrooms])
            try:
                bathrooms = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[2]').text
                bathrooms = float(re.findall('\d{1,}\.{0,1}\d{0,1}',bathrooms)[0])
                t_bathrooms.extend([bathrooms])
            except:
                t_bathrooms.extend(['NA'])
            try:
                area = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[3]').text
                area = area.replace(',','')
                area = float(re.findall('\d{1,}\d{0,1}',area)[0])
                t_area.extend([area])
            except:
                t_area.extend(['NA'])
            try:
                item_type = item.find_element_by_xpath('.//ul[@class="list-card-details"]/li[4]').text
                item_type = item_type.strip().replace('-',' ').strip()
                t_item_type.extend([item_type])
            except :
                t_item_type.extend(['NA'])
            try:
                address = item.find_element_by_xpath('.//address[@class="list-card-addr"]').text
                t_address.extend([address])
            except:
                t_address.extend(['NA'])
            try:
                item_link = item.find_element_by_xpath('.//a[@class="list-card-link list-card-link-top-margin"]')
                item_link = item_link.get_attribute("href")
                t_item_link.extend([item_link])
            except:
                item_link='NA'
                t_item_link.extend([item_link])
                counter+=1

            print(str(price)+'\t'+str(bedrooms)+'\t'+str(bathrooms)+'\t'+str(area)+str(item_type)+'\t'+str(address)+'\t'+t_item_link[-1])
    '''
    print('*'*100)
    driver.quit()
    time.sleep(2)
    driver = webdriver.Safari()

    for ilink in (t_item_link):

        driver.get(ilink)
        time.sleep(5)
        try:
            type=driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[1]/span[2]').text
            t_type.extend([type])
            #print(type)
        except:
            t_type.extend([np.nan])

        try:
            construction=driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[2]/span[2]').text
            t_construction.extend([construction])
            #print(construction)
        except:
            t_construction.extend([np.nan])

        try:
            heating=driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[3]/span[2]').text
            t_heating.extend([heating])
            #print(heating)
        except:
            t_heating.extend([np.nan])

        try:
            cooling=driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[4]/span[2]').text
            #print(cooling)
            t_cooling.extend(cooling)
        except:
            t_cooling.extend([np.nan])

        try:
            parking=driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[5]/span[2]').text
            t_parking.extend([parking])
            #print(parking)
        except:
            t_parking.extend([np.nan])

        try:
            hoa=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[6]/span[2]').text
            t_HOA.extend([hoa])
            #print(hoa)
        except:
            t_HOA.extend([np.nan])

        try:
            p_s=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[7]/span[2]').text
            t_p_s.extend([p_s])
            #print(p_s)
            #print('*' * 40)
        except:
            t_p_s.extend([np.nan])

        try:
            p_i=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[1]/div/div/div/div/span[2]').text
            t_p_i.extend([p_i])
            #print(p_i)
        except:
            t_p_s.extend([np.nan])

        try:
            mortgage=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[2]/div/div/div/div/span[2]').text
            t_mortgage.extend([mortgage])
            #print(mortgage)
        except:
            t_mortgage.extend([np.nan])

        try:
            tax=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[3]/div[1]/div/div/div/span[2]').text
            t_tax.extend([tax])
            #print(tax)
        except:
            t_tax.extend([np.nan])

        try:
            insurance=driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[4]/div/div/div/div/span[2]').text
            t_insurance.extend([insurance])
            #print(insurance)
        except:
            t_insurance.extend([np.nan])

        try:
            school=driver.find_elements_by_xpath('//*[@id="ds-data-view"]/ul/li[11]/div/div[1]/div[2]/ul/li')
            school_str=''
            for ischool in school:
                num=ischool.find_element_by_xpath('./div[1]/div/span[1]').text
                denum=ischool.find_element_by_xpath('./div[1]/div/span[2]').text
                denum=re.findall('\d{1,}',denum)[0]
                school_name=ischool.find_element_by_xpath('./div[2]/a').text
                #print(school_name)
                school_str=school_str+','+str(school_name)
            t_school.extend([school_str.strip()])
        except:
            t_school.extend([np.nan])


'''
    driver.quit()
    page_index +=1

d['Price'].extend(t_price)
d['Bedrooms'].extend(t_bedrooms)
d['Bathrooms'].extend(t_bathrooms)
d['Area'].extend(t_area)
d['Type'].extend(t_type)
d['Address'].extend(t_address)
d['link'].extend(t_item_link)

df1=pd.DataFrame(d['Price'])
df2=pd.DataFrame(d['Bedrooms'])
df3=pd.DataFrame(d['Bathrooms'])
df4=pd.DataFrame(d['Area'])
df5=pd.DataFrame(d['Type'])
df6=pd.DataFrame(d['Address'])
df7=pd.DataFrame(d['link'])

df1.to_csv('Price.csv')
df2.to_csv('Bedrooms.csv')
df3.to_csv('Bathrooms.csv')
df4.to_csv('Area.csv')
df5.to_csv('Type.csv')
df6.to_csv('Address.csv')
df7.to_csv('Link.csv')