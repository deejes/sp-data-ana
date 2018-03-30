import math
import simplejson
from asin_list_original import AsinList


def big_list_splitter(big_list,number_of_sublists):
    """ Takes a python list and splits it up into n sublists,
    and writes each to a file. """
    length_of_sublists = math.floor(len(big_list)/number_of_sublists)
    master_dict = {}
    names_list = []

    for x in range(1,number_of_sublists+1):
        name = 'asin_list' + str(x) +'.py'
        names_list.append(name)
        master_dict[name] = []
    # return names_list

    start = 0
    end = length_of_sublists

    for x in range(number_of_sublists):   
        """splits the list and stores it in the dictionary"""
        # this line gives the last sublist an additional modulo elements
        if x == number_of_sublists - 1:
            master_dict[names_list[x]] = big_list[start:]
        else:        
            master_dict[names_list[x]] = big_list[start:end]
            start += length_of_sublists
            end += length_of_sublists

    for name in names_list:
        """writes lists to {name}.py"""
        with open (name, 'wt') as filename:
            simplejson.dump( master_dict[name],filename)
        print (len(master_dict[name])) # logs number of elements

    for name in names_list:
        """adds name before list in each file"""
        with open(name, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write( name[:-3] + ' = ' + content)

    with open('names_list.py', 'wt') as filename:
        simplejson.dump( names_list,filename)


        
        
# from asin_list1 import asin_list1
# print (len(asin_list1))

big_list_splitter(AsinList,10)
