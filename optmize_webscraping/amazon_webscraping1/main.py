from multiprocessing import Process
from scrape_url_function import scrape_urls_list

names_list = ['asin_list1', 'asin_list2', 'asin_list3', 'asin_list4', 'asin_list5', 'asin_list6', 'asin_list7', 'asin_list8', 'asin_list9', 'asin_list10']


def echo(input_list, errors_output_file, results_output_file):
    print (input_list[0])

    with open(errors_output_file, 'at') as myfile:
        myfile.write("hello output file!")
    
    with open(results_output_file, 'at') as myfile:
        myfile.write("hello results file!")
    


a = [1,2,3]
b = "errors.txt"
c = "results.txt"


def start_scrape_workers(n):  
    for _ in range(n):
        request_worker_process = Process(target=echo,
                                        #  args=(input_list,errors_output_file,results_output_file))
                                         args=(a,b,c))
        request_worker_process.start()


start_scrape_workers(1)

