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

for i in asin_list:
    url = "http://www.amazon.com/dp/"+i
    print ("Processing: "+url)
    single_url_data = (parse(url))
    import pdb; pdb.set_trace()
    write_to_csv(single_url_data)
    # extracted_data.append(parse(url))
    sleep(1)
