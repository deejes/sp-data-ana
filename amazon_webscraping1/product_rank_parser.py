def parse_product_rank(li_element_list):
    ### Takes a list of elements from best seller info, returns relevant comma separated values
    li_element_list = [x.strip() for x in li_element_list]
    result = []
    for element in li_element_list[:]:
        if len(element) > 1 and "{" not in element and ":" not in element:
            result.append(element)
    return (",".join(result))