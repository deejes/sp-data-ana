import random
import csv,os,json
import requests
from time import sleep
from lxml import html
from parse_amazon_webpage import parse
from write_to_file import initalise_write_headers, write_row

#TODO - add error logs

def scrape_urls_list(input_list, errors_output_file, results_output_file):

    # Returns the index of the last processed ASN 
    with open(results_output_file,'r') as myfile:
        reader = csv.reader(myfile)
        last_asn = (list(reader)[-1][-2][-10:])
    last_asn_index = AsinList.index(last_asn)


    


    for i in AsinList[last_asn_index+1:]:
        url = "http://www.amazon.com/dp/"+i
        print ("Processing: "+url)
        single_url_data = (parse(url,errors_output_file))
        write_row(single_url_data,results_output_file)
        # sleep(1)

