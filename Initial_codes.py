import re
from scrapy import Spider, Request

number_results=int(response.xpath('//span[@class="jsx-335803843 result-count"]/text()').extract()[0].replace(',',''))

items=response.xpath('//ul[@class="jsx-2910884806 property-list list-unstyle"]/li')

for item in items:

	try:

		price=int(item.xpath('.//div[@class="jsx-4195823209 price"]/span/text()').extract()[0].replace('$','').replace(',',''))
		number_bedroom=int(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[0])
		number_bathroom=int(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[1])
		area=int(item.xpath('.//span[@class="jsx-2256820618 meta-value"]/text()').extract()[2].repalce(',',''))
		lot_area=item.xpath('.//span[@class="jsx-2256820618 meta-label"]/text()').extract()[3]

		address_part1=item.xpath('.//div[@class="jsx-4195823209 address ellipsis"]/text()').extract()
		address_aprt2=item.xpath('.//div[@class="jsx-4195823209 address-second ellipsis"]/text()').extract()

		address_part1=[re.sub(' +',',',istring) for istring in address_part1]
		address_part1=''.join(address_part1)
		address_part2=[re.sub(' +',',',istring) for istring in address_part2]
		address_part2=''.join(address_part2)

		address=address_part1+address_part2

		link1='https://www.realtor.com'
		link2=item.xpath('.//div[@class="jsx-4195823209 detail-wrap has-cta fixed-wrapper"]/a/@href').extract()[0]
		item_link=link1+link2

		yield Request(url=item_link,callback=parse_item)

		nearby_school=response.xpath('//table[@class="table table-clear table-heading-unstyled table-school school-rating-lg"]/tbody/tr')

		for ischool in nearby_school:

			school_rating=ischool.xpath('.//td[1]/span/text()').extract()[0]
			school_name=ischool.xpath('.//td[2]/a/text()').extract()
			school_grade=ischool.xpath('.//td[3]/text()').extract()
			school_distance=re.findall('\d+\.*\d+',ischool.xpath('.//td[4]/text()').extract()[0])

		neighborhod=item.xpath('//div[@class="neighborhood-flex-item"]/div')
		number_neighborhod=len(neighborhod)-2

		median_neighborhod=[re.findall('\d+',x.replace(',','').replace('$','')) for x in neighbors.xpath('./text()').extract()[2:]]

		nearby_homes=response.xpath('//ul[@class="list-unstyled nearby-homevalues-properties"]/li')

		for ihome in nearby_homes[1:]:

			nearby_homes_price.extend(re.sub(' +','',tags[1].xpath('./div[1]/text()').extract()[0].replace('$','').replace(',','')))
			nearby_homes_bedroom.extend(re.sub(' +','',tags[1].xpath('./div[2]/text()').extract()[0].replace('$','').replace(',','')))
            nearby_homes_bathroom.extend(re.sub(' +','',tags[1].xpath('./div[3]/text()').extract()[0].replace('$','').replace(',','')))
            nearby_homes_area.extend(re.sub(' +','',tags[1].xpath('./div[4]/text()').extract()[0].replace('$','').replace(',','')))
            nearby_homes_lot_area.extend(re.sub(' +','',tags[1].xpath('./div[5]/text()').extract()[0].replace('$','').replace(',','')))



        response.xpath('//div[@class="neighborhood-flex-container padding-bottom"]/div/p/text()').extract()



