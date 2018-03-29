import random
import csv,os,json
import requests
from time import sleep
from lxml import html
from parse_amazon_webpage import parse
from write_to_file import initalise_write_headers, write_row



# asin_list = []
# for _ in range (10):
#     asin_list.append(AsinList[random.randint(0,len(AsinList))])

#TODO - add error logs

def scrape_urls_list(input_list, errors_output_file, results_output_file):
    initalise_write_headers(results_output_file)
    with open(results_output_file,'r') as myfile:
        reader = csv.reader(myfile)
        last_asn = (list(reader)[-1][-2][-10:])
        # import pdb; pdb.set_trace()

    last_asn_index = AsinList.index(last_asn)
    for i in AsinList[last_asn_index+1:]:
        url = "http://www.amazon.com/dp/"+i
        print ("Processing: "+url)
        single_url_data = (parse(url))
        write_row(single_url_data,results_output_file)
        # sleep(1)

