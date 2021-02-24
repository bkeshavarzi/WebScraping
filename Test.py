import numpy as np
import pandas as pd
import re
import selenium
from selenium import webdriver
import time

'''
address = "238 Grand Canal, CA 92620"
link = "https://www.gps-coordinates.net"
driver = webdriver.Safari()
driver.get(link)
time.sleep(4)
input_address = driver.find_element_by_xpath('//*[@id="address"]')
input_address.send_keys(address)
button_action = driver.find_element_by_xpath('//div[@class="col-md-4"]/button[@class="btn btn-primary"]')
button_action.click()
time.sleep(10)
driver.execute_script("window.scrollTo(0, 1000)")
'''

s=['1-60','60-120','120-180','180-240','240-300','300-360','360-420','420-480','480-540','540-600','600-660','660-700','700-720','720-730','730-740','740-799']
t_type = []  # done
t_construction = []  # done
t_heating = []  # done
t_parking = []  # done
t_HOA = []
t_p_s = []
t_p_i = []
t_mortgage = []
t_tax = []
t_insurance = []
t_school = []
t_school_ranking = []

dict_={'Type':t_type,'Construction':t_construction,'Parking':[],'Heating':t_heating,'HOA':t_HOA,'Price_SQFT':t_p_s,'Principal_Interest':t_p_i,
       'Mortgage':t_mortgage,'Tax':t_tax,'Insurance':t_insurance,'School':t_school,'Ranking':t_school_ranking}

for istring in range(len(s)):

    t=pd.read_csv('Type'+s[istring]+'.csv').iloc[:,1].values
    construction=pd.read_csv('Construction'+s[istring]+'.csv').iloc[:,1].values
    heating=pd.read_csv('Heating'+s[istring]+'.csv').iloc[:,1].values
    parking=pd.read_csv('Parking'+s[istring]+'.csv').iloc[:,1].values
    hoa=pd.read_csv('HOA'+s[istring]+'.csv').iloc[:,1].values
    price_sqft=pd.read_csv('Price_SQFT'+s[istring]+'.csv').iloc[:,1].values
    price_i=pd.read_csv('Price_i'+s[istring]+'.csv').iloc[:,1].values
    mortgage=pd.read_csv('Mortgage'+s[istring]+'.csv').iloc[:,1].values
    tax = pd.read_csv('Tax' + s[istring] + '.csv').iloc[:, 1].values
    insurance=pd.read_csv('Insurance' + s[istring] + '.csv').iloc[:, 1].values
    school=pd.read_csv('School' + s[istring] + '.csv').iloc[:, 1].values
    rating=pd.read_csv('School_ranking' + s[istring] + '.csv').iloc[:, 1].values

    t_type.extend(t)
    t_construction.extend(construction)
    t_heating.extend(heating)
    t_parking.extend(parking)
    t_HOA.extend(hoa)
    t_p_s.extend(price_sqft)
    t_p_i.extend(price_i)
    t_mortgage.extend(mortgage)
    t_tax.extend(tax)
    t_insurance.extend(insurance)
    t_school.extend(school)
    t_school_ranking.extend(rating)

dict_['Type']=t_type
dict_['Construction']=t_construction
dict_['Heating']=t_heating
dict_['Parking']=t_parking
dict_['HOA']=t_HOA
dict_['Price_SQFT']=t_p_s
dict_['Principal_Interest']=t_p_i
dict_['Mortgage']=t_mortgage
dict_['Tax']=t_tax
dict_['Insurance']=t_insurance
dict_['School']=t_school
dict_['Ranking']=t_school_ranking

df=pd.DataFrame(dict_)
df.to_csv('Zillow_NYC_Data.csv')





