from scrapy import Spider, Request
from Realtor.items import RealtorItem
import re
import time

class RealtorSpider(Spider):
    
    name='realtor_spider'
    allowed_domains = ['www.realtor.com']
    start_urls = ['https://www.realtor.com/realestateandhomes-search/Raleigh_NC']

    def parse(self,response):

        numberitems=int(response.xpath('//span[@class="jsx-335803843 result-count"]/text()').extract()[0].replace(',',''))
        total_pages=int(response.xpath('//div[@class="sc-pkIrX hKjnPC"]/a/text()').extract()[1:-1][-1])
        link1='www.realtor.com'

        for ipage in range(1,4) :#total_pages+1):

            #time.sleep(20)
            url = 'https://www.realtor.com/realestateandhomes-search/Raleigh_NC/pg-'+str(ipage)
            print('Parsing page='+str(ipage))
            yield Request(url=url,callback=self.parse_page)

    def parse_page(self,response):

        items=response.xpath('//ul[@class="jsx-2910884806 property-list list-unstyle"]/li')

        for item in items:

            print('*'*40)

            try:

                price=int(item.xpath('.//div[@class="jsx-4195823209 price"]/span/text()').extract()[0].replace('$','').replace(',',''))
                print('Price is:'+str(price))

            except:

                print('Not an option, price is not available!!')

            try:

                itemtype=item.xpath('.//span[@class="jsx-4195823209"]/text()').extract()[0]
                print('Type is:'+str(itemtype))

            except:

                itemtype="NA"

            try:

                bedroom=int(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[0])
                print('Bedroom is'+str(bedroom))

            except:

                bedroom="NA"

            try:

                bathroom=float(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[1])
                print('Bathroom is:'+str(bathroom))

            except:

                bathroom="NA"

            try:

                area=int(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[2].replace(',',''))
                print('Area is:'+str(area))

            except:

                area="NA"

            try:

                area_lot=float(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[3].replace(',',''))
                print('Area lot is'+str(area_lot))

            except:

                area_lot="NA"

            try:

                address_part1=item.xpath('.//div[@class="jsx-4195823209 address ellipsis"]/text()').extract()
                address_part2=item.xpath('.//div[@class="jsx-4195823209 address-second ellipsis"]/text()').extract()
                address_part1=[re.sub(' +',',',istring) for istring in address_part1]
                address_part1=''.join(address_part1)
                address_part2=[re.sub(' +',',',istring) for istring in address_part2]
                address_part2=''.join(address_part2)
                address=address_part1+address_part2
                print('Address is'+str(address))

            except:

                address="NA"

            try:

                link2=item.xpath('.//div[@class="jsx-4195823209 detail-wrap has-cta fixed-wrapper"]/a/@href').extract()[0]
                item_link='www.realtor.com'+link2
                print('Link is:   '+str(item_link))
                yield Request(url=item_link,meta={'price':price,'type':itemtype,'bed':bedroom,'bath':bathroom,'area':area,'area_lot':area_lot,'address':address},callback=self.parse_item_page)
                #yield Request(url=item_link,callback=self.parse_item_page)
                

            except:

                print('Not an option, Link is not available!!')


    def parse_item_page(self,response):


        nearby_school=response.xpath('////div[@class="jsx-2161498733 content hide"]/table/tbody/tr')
        school_data={'rating':[],'name':[],'grade':[],'distance':[]}

        print("Number of nearby school is :"+str(len(nearby_school)))


        for counter,ischool in enumerate(nearby_school):

            try:

                school_rating=float(ischool.xpath('./td[1]/span/span/text()').extract()[0])/float(ischool.xpath('./td[1]/span/span/sub/text()').extract()[0].replace('/',''))
                school_data['rating'].extend([school_rating])
                print("School #"+str(counter)+", rating is: "+str(school_rating))

            except:

                school_data['rating'].extend(['NA'])

            try:

                school_name=ischool.xpath('.//td[2]/a/text()').extract()[0]
                school_data['name'].extend([school_name])
                print("School #"+str(counter)+", name is: "+str(school_name))

            except:

                school_data['name'].extend(['NA'])

            try:

                school_grade=ischool.xpath('.//td[3]/span/text()').extract()[1]
                school_data['grade'].extend([school_grade])
                print("School #"+str(counter)+", grade is: "+school_name)

            except:

                school_data['grade'].extend(['NA'])

            try:

                school_distance=float(ischool.xpath('.//td[4]/span/text()').extract()[1])
                school_data['distance'].extend([school_distance])
                print("School #"+str(counter)+", distance is: "+str(school_distance))

            except:

                school_data['distance'].extend(['NA'])

        try:

            neighborhood,city=response.xpath('//div[@class="jsx-2161498733 content hide"]/div/div/p/a/text()').extract()[:2]
            print('Neighborhood is: '+neighborhood)
            print('City is: '+city)

        except:

            neighborhood='NA'
            city='NA'

        
        try:

            median_listing_price=float(response.xpath('//div[@class="jsx-2161498733 content hide"]/div/div[2]/ul/li[1]/text()').extract()[0].replace('$','').replace(',',''))
            print('median_listing_price is: '+str(median_listing_price))

        except:

            median_listing_price="NA"

        try:

            median_price_sqft=float(response.xpath('//div[@class="jsx-2161498733 content hide"]/div/div[2]/ul/li[2]/text()').extract()[0].replace('$','').replace(',',''))
            print('median_listing_price is: '+str(median_price_sqft))

        except:

            median_price_sqft="NA"
        
        try:

            neighborhood_around=response.xpath('//div[@class="jsx-2161498733 content hide"]/div/div[2]/div/ul/li')
            neighborhood_name_price={'Name':[],'Price':[]}

            for counter,ineighbor in enumerate(neighborhood_around):

                temp_name=ineighbor.xpath('./a/text()').extract()[0]
                temp_price=float(ineighbor.xpath('./span/span/text()').extract()[0].replace('$','').replace(',',''))
                neighborhood_name_price['Name'].extend([temp_name])
                neighborhood_name_price['Price'].extend([temp_price])
                print('For Neighborhood #'+str(counter)+"Name is: "+temp_name+"and price is: "+str(temp_price))

        except:

            neighborhood_name_price={'Name':[],'price':[]}


        item=RealtorItem()

        item['price']=meta['price']
        item['item_type']=meta['type']
        item['bedroom']=meta['bed']
        item['bathroom']=meta['bath']

        item['area']=meta['area']
        item['area_lot']=meta['area_lot']
        item['address']=meta['address']
      

        item['school_data']=school_data
        item['neighborhood']=neighborhood
        item['city']=city
        item['neighborhood_data']={"price":median_listing_price,"price_sqft":median_price_sqft}
        item['nearby_neighborhoods_data']=neighborhood_name_price

        yield item



