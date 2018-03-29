from multiprocessing import Process
from scrape_url_function import scrape_urls_list

names_list = ['asin_list1', 'asin_list2', 'asin_list3', 'asin_list4', 'asin_list5', 'asin_list6', 'asin_list7', 'asin_list8', 'asin_list9', 'asin_list10']

def start_scrape_workers(10):  # starts n workers to process the queue
    for _ in range(n):
        request_worker_process = Process(target=scrape_urls_list,
                                         args=(input,response_queue,acceptable_website_response_wait))
        request_worker_process.start()


start_request_workers(num_request_workers)

