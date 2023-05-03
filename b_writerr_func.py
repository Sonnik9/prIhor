import b_filter_func

def b_w_writerr(black_list, n1, n2):
    import json
    print("hello black writer")
    try:
        new_resBlackList = eval(b_filter_func.black_filter(black_list))
    except Exception as ex:
        print(f"339____{ex}")
        new_resBlackList = black_list

    if new_resBlackList != None and new_resBlackList != []:
        print(f"len_resBlackList___{len(new_resBlackList)}")
        try:
            with open(f'black_list_{n1}___{len(new_resBlackList)}.json', "w", encoding="utf-8") as file: 
                json.dump(new_resBlackList, file, indent=4, ensure_ascii=False)
        except Exception as ex:
            print(f"str348__{ex}")