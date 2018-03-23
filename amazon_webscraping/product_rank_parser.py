a = ['\n', 'Amazon Best Sellers Rank:', ' \n\n\n\n \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', '\n.zg_hrsr { margin: 0; padding: 0; list-style-type:none; }\n.zg_hrsr_item { margin: 0 0 0 10px; }\n.zg_hrsr_rank { display: inline-block; width: 80px; text-align: right; }\n', '\n\n', '\n    ', '\n    ', '#47', '\n    ', u'in\xa0', 'Health & Household', ' > ', 'Sexual Wellness', ' > ', 'Adult Toys & Games', ' > ', 'Sex Toys', ' > ', 'Penis Rings', '\n    ', '\n', '\n\n']
b = [x.strip() for x in a]



def parse_product_rank(li_element_list):
    # filters = [ "{" , "\\" ,"\>"]
    result = []
    for element in li_element_list[:]:
        if len(element) > 1 and "{" not in element and ":" not in element:
            print (element)
        # useless = True
        # # for filter_char in filters:
        #     if filter_char in element.strip():
        #         useless = False
        # if not useless:
        #     result.append(element)
    import pdb; pdb.set_trace()
    print (" ".join(result))




parse_product_rank(b)