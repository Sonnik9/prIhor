def black_filter(finRes):
    d_lackList = []
    sorted_blackList = []
    refactor_blackList = []
    # try:
    #     resBlackList = eval(finRes)
    # except Exception as ex:
    #     print(f"308____{ex}")
    #     resBlackList = finRes

    for t in finRes:
        try:
           d_lackList.append(t[2])
        except:
            continue
    try:
        d_lackList = list(filter(None, d_lackList))                
        d_lackList = list(filter([], d_lackList))
    except Exception as ex:
        print(f"315____{ex}")
    try:
        for lst in d_lackList:
            merged_dict = {}
            for dct in lst:
                hotel_id = dct["hotel_id"]
                url = dct["url"]
                if hotel_id not in merged_dict:
                    merged_dict[hotel_id] = {"hotel_id": hotel_id, "url": url}
                merged_dict[hotel_id][list(dct.keys())[2]] = dct[list(dct.keys())[2]]
            sorted_blackList.append(list(merged_dict.values()))
        for item in sorted_blackList:
            refactor_blackList += item

    except Exception as ex:
        print(f"327____{ex}")
    try:
        return refactor_blackList
    except Exception as ex:
        print(f"331____{ex}")
        return None

