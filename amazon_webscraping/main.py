from lxml import html
import csv,os,json
import requests
from time import sleep
from parse_amazon_webpage import parse
from asin_list import AsinList
import random

asin_list = []
for _ in range (10):
    asin_list.append(AsinList[random.randint(0,len(AsinList))])

# asin_list = ["B01LWOC3JO"]
# http://www.amazon.com/dp/

# extracted_data = []


for i in asin_list:
    url = "http://www.amazon.com/dp/"+i
    print ("Processing: "+url)
    single_url_data = (parse(url))
    import pdb; pdb.set_trace()
    # extracted_data.append(parse(url))
    sleep(1)
# f=open('data.json','w')
# json.dump(extracted_data,f,indent=4)


# if __name__ == "__main__":
#     ReadAsin()