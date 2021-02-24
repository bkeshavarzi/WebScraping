import numpy as np
import pandas as pd
import re
import selenium
from selenium import webdriver
import time

df=pd.read_csv('Link.csv')
counter=0

t_type = []  # done
t_construction = []  # done
t_heating = []  # done
t_cooling = []  # done
t_parking = []  # done
t_HOA = []
t_p_s = []
t_p_i = []
t_mortgage = []
t_tax = []
t_insurance = []
t_school = []
t_school_ranking = []

driver = webdriver.Safari()
start_index=740
end_index=799

for ilink in df.iloc[:,1][start_index:end_index]:

    driver.get(ilink)
    time.sleep(5)

    try:
        type = driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[1]/span[2]').text
        t_type.extend([type])
    except:
        t_type.extend([np.nan])

    try:
        construction = driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[2]/span[2]').text
        t_construction.extend([construction])
    except:
        t_construction.extend([np.nan])

    try:
        heating = driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[3]/span[2]').text
        t_heating.extend([heating])
    except:
        t_heating.extend([np.nan])

    try:
        parking = driver.find_element_by_xpath('//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[5]/span[2]').text
        t_parking.extend([parking])
    except:
        t_parking.extend([np.nan])

    try:
        hoa = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[6]/span[2]').text
        t_HOA.extend([hoa])
    except:
        t_HOA.extend([np.nan])

    try:
        p_s = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[5]/div/div/div[1]/ul/li[7]/span[2]').text
        t_p_s.extend([p_s])
    except:
        t_p_s.extend([np.nan])

    try:
        p_i = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[1]/div/div/div/div/span[2]').text
        t_p_i.extend([p_i])
    except:
        t_p_i.extend([np.nan])

    try:
        mortgage = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[2]/div/div/div/div/span[2]').text
        t_mortgage.extend([mortgage])
    except:
        t_mortgage.extend([np.nan])

    try:
        tax = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[3]/div[1]/div/div/div/span[2]').text
        t_tax.extend([tax])
    except:
        t_tax.extend([np.nan])

    try:
        insurance = driver.find_element_by_xpath('.//*[@id="ds-data-view"]/ul/li[9]/div/div[1]/div/div[2]/div[4]/div/div/div/div/span[2]').text
        t_insurance.extend([insurance])
    except:
        t_insurance.extend([np.nan])

    try:
        school = driver.find_elements_by_xpath('.//li[@class="sc-pkIrX bOdyGc"]')
        school_str = ''
        rating= ''
        for ischool in school:
            num = ischool.find_element_by_xpath('./div[1]/div/span[1]').text.strip()
            denum = ischool.find_element_by_xpath('./div[1]/div/span[2]').text
            denum = re.findall('\d{1,}', denum)[0].strip()
            rating=rating+str(float(num)/float(denum))+','
            school_name = ischool.find_element_by_xpath('./div[2]/a').text.strip()
            school_str = school_str + '-' + str(school_name)+','
        t_school.extend([school_str.strip()])
        t_school_ranking.extend([rating.strip()])
        #print(school_str)
        #print(rating)
        #print('*'*200)

    except:
        t_school.extend(['NA'])
        t_school_ranking.extend(['NA'])
    print(str(t_type[-1])+'\t'+str(t_construction[-1])+'\t'+str(t_heating[-1])+'\t'+str(t_parking[-1])+'\t'+str(t_HOA[-1])+'\t'+str(t_p_s[-1])+'\t'+str(t_p_i[-1])+'\t'+str(t_mortgage[-1])+'\t'+str(t_tax[-1])+'\t'+str(t_insurance[-1])+'\t'+
          str(t_school[-1])+'\t'+str(t_school_ranking[-1]))

df1=pd.DataFrame(t_type)
df2=pd.DataFrame(t_construction)
df3=pd.DataFrame(t_heating)
df4=pd.DataFrame(t_parking)
df5=pd.DataFrame(t_HOA)
df6=pd.DataFrame(t_p_s)
df7=pd.DataFrame(t_p_i)
df8=pd.DataFrame(t_mortgage)
df9=pd.DataFrame(t_tax)
df10=pd.DataFrame(t_insurance)
df11=pd.DataFrame(t_school)
df12=pd.DataFrame(t_school_ranking)



name_type='Type'+str(start_index)+str('-')+str(end_index)+'.csv'
name_construction='Construction'+str(start_index)+str('-')+str(end_index)+'.csv'
name_heating='Heating'+str(start_index)+str('-')+str(end_index)+'.csv'
name_parking='Parking'+str(start_index)+str('-')+str(end_index)+'.csv'
name_hoa='HOA'+str(start_index)+str('-')+str(end_index)+'.csv'
name_price_sqft='Price_SQFT'+str(start_index)+str('-')+str(end_index)+'.csv'
name_price_i='Price_i'+str(start_index)+str('-')+str(end_index)+'.csv'
name_mortgage='Mortgage'+str(start_index)+str('-')+str(end_index)+'.csv'
name_tax='Tax'+str(start_index)+str('-')+str(end_index)+'.csv'
name_insurance='Insurance'+str(start_index)+str('-')+str(end_index)+'.csv'
name_school='School'+str(start_index)+str('-')+str(end_index)+'.csv'
name_rating='School_ranking'+str(start_index)+str('-')+str(end_index)+'.csv'

df1.to_csv(name_type)
df2.to_csv(name_construction)
df3.to_csv(name_heating)
df4.to_csv(name_parking)
df5.to_csv(name_hoa)
df6.to_csv(name_price_sqft)
df7.to_csv(name_price_i)
df8.to_csv(name_mortgage)
df9.to_csv(name_tax)
df10.to_csv(name_insurance)
df11.to_csv(name_school)
df12.to_csv(name_rating)

driver.quit()