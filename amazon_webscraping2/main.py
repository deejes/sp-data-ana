import random
import csv,os,json
import requests
from time import sleep
from lxml import html
from parse_amazon_webpage import parse
from asin_list import AsinList2
from write_to_file import initalise_write_headers, write_row



# asin_list = []
# for _ in range (10):
#     asin_list.append(AsinList[random.randint(0,len(AsinList))])

#TODO - add error logs
initalise_write_headers()

# import pdb; pdb.set_trace()

# last_asn_index = 0

with open('amazon_data.csv','r') as myfile:
    reader = csv.reader(myfile)
    last_asn = (list(reader)[-1][-2][-10:])

# import pdb; pdb.set_trace()

last_asn_index = AsinList2.index(last_asn)

for i in AsinList2[last_asn_index+1:]:
    url = "http://www.amazon.com/dp/"+i
    print ("Processing: "+url)
    single_url_data = (parse(url))
    write_row(single_url_data)
    # sleep(1)

