import math
import simplejson

from asin_list_original import AsinList

big_list = AsinList

number_of_sublists = 10

length_of_sublist = math.floor(len(big_list)/number_of_sublists)

print (length_of_sublist)

master_dict = {}
names_list = []

for x in range(1,number_of_sublists+1):
    name = 'asin_list' + str(x)
    names_list.append(name)
    master_dict[name] = []

# print (master_dict,names_list)

start = 0
end = length_of_sublist

for x in range(number_of_sublists):
    if x == number_of_sublists - 1:
        master_dict[names_list[x]] = big_list[start:]
    else:        
        master_dict[names_list[x]] = big_list[start:end]
        start += length_of_sublist
        end += length_of_sublist

# for name in names_list:
#     with open (name+'.txt', 'wt') as filename:
#         simplejson.dump(master_dict[name],filename)
#     print (len(master_dict[name]))


print (names_list)