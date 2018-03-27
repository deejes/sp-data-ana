import random
import csv,os,json
import requests
from time import sleep
from lxml import html
from parse_amazon_webpage import parse
from asin_list import AsinList
from write_to_file import initalise_write_headers, write_row



asin_list = []
for _ in range (10):
    asin_list.append(AsinList[random.randint(0,len(AsinList))])

#TODO - add error logs
initalise_write_headers()

for i in asin_list:
    url = "http://www.amazon.com/dp/"+i
    print ("Processing: "+url)
    single_url_data = (parse(url))
    write_row(single_url_data)
    import pdb; pdb.set_trace()
    sleep(1)

