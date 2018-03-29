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


def initalise_write_headers(results_output_file):
    my_file = Path("./" + results_output_file)
    if not my_file.is_file():
        with open(results_output_file, 'wt') as myfile:
            wr = csv.writer(myfile)
            wr.writerow(headers)

# input_list = ['Fetish Fantasy Series Japanese Silk Rope, 35 Feet, Erotic Pink', 'http://www.amazon.com/dp/B00IF238UE', '#1,674,724 in Health & Household (,See Top 100 in Health & Household']
# input_list_2 = ['Sex Ties & Bondage Tape - Black', '$9.16', 'Health & Household > Sexual Wellness > Bondage Gear & Accessories > Restraints', '$9.16', 'In Stock.', 'http://www.amazon.com/dp/B00B6KSDMK', None]

def write_row(amz_webpage_metrics,results_output_file):
    # Takes a list of amazon webpage metrics, appends to amazon_data.csv
    amz_webpage_metrics = [0 if e is None else e for e in amz_webpage_metrics]
    with open(results_output_file, 'at') as myfile:
        wr = csv.writer(myfile,quoting=1)
        wr.writerow(amz_webpage_metrics)


# initalise_write_headers()
# write_row(input_list_2)



