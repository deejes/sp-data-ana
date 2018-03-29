from lxml import html
import csv,os,json
import requests
from time import sleep

def parse_product_rank(li_element_list):
    ### Takes a list of elements from best seller info, returns relevant comma separated values
    li_element_list = [x.strip() for x in li_element_list]
    result = []
    for element in li_element_list[:]:
        if len(element) > 1 and "{" not in element and ":" not in element:
            result.append(element)
    return (",".join(result))


def parse(url):
    """ Takes a amazon/dp/asn url, returns a dictonary containing page metrics"""
    # headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    }

    page = requests.get(url,headers=headers)
    for i in range(20):
        try:
            # import pdb; pdb.set_trace()
            doc = html.fromstring(page.content)
            XPATH_NAME = '//h1[@id="title"]//text()'
            XPATH_ORIGINAL_PRICE = '//*[@class="a-text-strike"]//text()'
            XPATH_SALE_PRICE = '//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()'
            XPATH_CATEGORY = '//a[@class="a-link-normal a-color-tertiary"]//text()'
            XPATH_AVAILABILITY = '//span[@id="availability"]//text() | //*[@id="availability"]/span//text()'
            XPATH_PRODUCT_RANK = '//*[@id="SalesRank"]//text()'
            RAW_NAME = doc.xpath(XPATH_NAME)
            RAW_SALE_PRICE = doc.xpath(XPATH_SALE_PRICE)
            RAW_CATEGORY = doc.xpath(XPATH_CATEGORY)
            RAW_ORIGINAL_PRICE = doc.xpath(XPATH_ORIGINAL_PRICE)
            RAw_AVAILABILITY = doc.xpath(XPATH_AVAILABILITY)
            RAW_PRODUCT_RANK = doc.xpath(XPATH_PRODUCT_RANK)
            NAME = ' '.join(''.join(RAW_NAME).split()) if RAW_NAME else None
            SALE_PRICE = ' '.join(''.join(RAW_SALE_PRICE).split()).strip() if RAW_SALE_PRICE else None
            CATEGORY = ' > '.join([i.strip() for i in RAW_CATEGORY]) if RAW_CATEGORY else None
            ORIGINAL_PRICE = ''.join(RAW_ORIGINAL_PRICE).strip() if RAW_ORIGINAL_PRICE else None
            AVAILABILITY = ''.join(RAw_AVAILABILITY).strip() if RAw_AVAILABILITY else None
            PRODUCT_RANK = parse_product_rank(RAW_PRODUCT_RANK) if RAW_PRODUCT_RANK else None
            # import pdb; pdb.set_trace()            
            if not ORIGINAL_PRICE:
                ORIGINAL_PRICE = SALE_PRICE
            
            if page.status_code == 503:
                sleep(10)
                raise ValueError('captcha')
            
            if page.status_code == 404:
                print(url,"not found. remove from asin list")
                with open('asn_not_found.txt', 'at') as myfile:
                    myfile.write(str(url)+"\n")
                # TODO - log asin with 404
                return ([0 for _ in range(7) ])

            data =[ NAME,
                    SALE_PRICE,
                    CATEGORY,
                    ORIGINAL_PRICE,
                    AVAILABILITY,
                    url,
                    PRODUCT_RANK
            ]

            return data
        except Exception as e:
            print (e)
