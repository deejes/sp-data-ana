from lxml import html
import csv,os,json
import requests
from time import sleep
from parse_amazon_webpage import parse


asin_list = ['B000000YGZ']

# extracted_data = []


for i in asin_list:
    url = "http://www.amazon.com/dp/"+i
    print ("Processing: "+url)
    print (parse(url))
    # extracted_data.append(parse(url))
    # sleep(5)
# f=open('data.json','w')
# json.dump(extracted_data,f,indent=4)


# if __name__ == "__main__":
#     ReadAsin()