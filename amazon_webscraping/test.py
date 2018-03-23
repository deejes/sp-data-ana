from asin_list import AsinList

# import pdb; pdb.set_trace()

# Given a sorted array of integers and a target value, determine if there exists two integers in the array that sum up to the target value.


import random

arr = [1]

for _ in range(1000):
    arr.append(arr[-1]+random.randint(1,19))

first = (arr[random.randint(0,len(arr))])  
second = (arr[random.randint(0,len(arr))])
rand_sum =  first + second


def sum_elements(arr,value):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i]+arr[j] == value:
            return (arr[i]+arr[j])
        elif arr[i]+arr[j] < value:
            i += 1
        else:
            j -= 1

print (sum_elements(arr,rand_sum) == first+second)