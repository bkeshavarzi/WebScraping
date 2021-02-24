import numpy as np
import pandas as pd
import re
import selenium
from selenium import webdriver
import time

fileid=1
df=pd.read_csv('OutPut1.csv')

t_zelle_estimate_month=[]
t_construction=[]
t_heating=[]
t_cooling=[]
t_garage=[]
t_hoa=[]
t_lot=[]
t_price_area=[]
driver = webdriver.Safari()
driver.get("https://www.zillow.com/homedetails/41-13-57th-St-Woodside-NY-11377/2076902099_zpid/")

for ilink in df['Link']:
#
#    print(ilink)
#
     try:
         z_estimate = driver.find_element_by_xpath('.//div[@class="sc-qQmou jqDvEh"]/span[2]').text
         z_estimate = re.findall('\d{1,}\,{0,1}\d{0,}', z_estimate)[0]
         z_estimate = z_estimate.replace(',','')
         t_zelle_estimate_month.extend([z_estimate])
     except:
         t_zelle_estimate_month.extend(['NA'])

     try:
         #facts_feature_button = driver.find_element_by_xpath('.//a[@class="hdp__mg5mjz-5 jgIHSZ"]')
         #facts_feature_button.click()
         time.sleep(10)
         construction=driver.find_element_by_xpath('.//span[@class="Text-c11n-8-18-0__aiai24-0 foiYRz"]').text
         t_construction.extend([construction])
     except:
         t_construction.extend(['NA'])

     print(str(t_zelle_estimate_month[-1])+'\t'+str(t_construction[-1]))
     #time.sleep(5)
     break
driver.quit()