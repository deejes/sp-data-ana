import csv
from pathlib import Path

headers = ['NAME',
           'SALE_PRICE',
           'CATEGORY',
           'ORIGINAL_PRICE',
           'AVAILABILITY',
           'url',
           'PRODUCT_RANK'
          ]     


def initalise_write_headers():
    my_file = Path("./amazon_data.txt")
    if not my_file.is_file():
        with open('amazon_data.txt', 'wt') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(headers)

input_list = ['Fetish Fantasy Series Japanese Silk Rope, 35 Feet, Erotic Pink', 'http://www.amazon.com/dp/B00IF238UE', '#1,674,724 in Health & Household (,See Top 100 in Health & Household']

def write_row(amz_webpage_metrics):
    with open('amazon_data.txt', 'at') as myfile:
        wr = csv.writer(myfile)
        # import pdb; pdb.set_trace()
        wr.writerow(amz_webpage_metrics)

write_row(input_list)