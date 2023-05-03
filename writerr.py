

def writerr(total, n1, n2):
    # print('hello total')
    # from itertools import groupby
    import json
    # from collections import defaultdict
    print(len(total))
    # print(total)
    resPhoto = []
    resDescription = []
    resFacilities = []
    resRooms = []
    resRoomHighlights = []
    resRoomsBlock = []
    resWhiteList = []
    # resBlackList = []
    # new_resBlackList = []

    try:
        for t in total:
            try:
                resPhoto.append(t[0][0])
            except:
                continue 

            try:
                resPhoto = list(filter(None, resPhoto))
                resPhoto = list(filter("", resPhoto)) 
            except:
                pass
        for t in total:
            try:
                resDescription.append(t[0][1])
            except Exception as ex:
                print(f"writerr__str30__{ex}")
                continue 
            try:
                resDescription = list(filter(None, resDescription))
                resDescription = list(filter("", resDescription)) 
            except:
                pass

        for t in total:
            try:
               resFacilities.append(t[0][2])
            except:
                continue 
            try:
                resFacilities = list(filter(None, resFacilities))
                resFacilities = list(filter("", resFacilities)) 
            except:
                pass
        for t in total:
            try:
               resRooms.append(t[0][3])
            except:
                continue 
            try:
                resRooms = list(filter(None, resRooms))
                resRooms = list(filter("", resRooms)) 
            except:
                pass
        for t in total:
            try:
               resRoomsBlock.append(t[0][4])
            except:
                continue 
            try:
                resRoomsBlock = list(filter(None, resRoomsBlock))
                resRoomsBlock = list(filter("", resRoomsBlock)) 
            except:
                pass
        for t in total:
            try:
               resRoomHighlights.append(t[0][6])
            except:
                continue 
            try:
                resRoomHighlights = list(filter(None, resRoomHighlights))
                resRoomHighlights = list(filter("", resRoomHighlights)) 
            except:
                pass
        for t in total:
            try:
               resWhiteList.append(t[1])
            except:
                continue 
            try:
                resWhiteList = list(filter(None, resWhiteList))                
                resWhiteList = list(filter([], resWhiteList))
                # resWhiteList = list(filter([None], resWhiteList)) 
            except:
                pass 

        # for t in total:
        #     try:
        #        resBlackList.append(t[2])
        #     except:
        #         continue 
            # try:
            #     resBlackList = list(filter(None, resBlackList))                
            #     resBlackList = list(filter([], resBlackList))
            #     # resWhiteList = list(filter([None], resWhiteList)) 
            # except:
            #     pass

        
        # for lst in resBlackList:
        #     merged_dict = {}
        #     for dct in lst:
        #         hotel_id = dct["hotel_id"]
        #         url = dct["url"]
        #         if hotel_id not in merged_dict:
        #             merged_dict[hotel_id] = {"hotel_id": hotel_id, "url": url}
        #         merged_dict[hotel_id][list(dct.keys())[2]] = dct[list(dct.keys())[2]]
        #     new_resBlackList.append(list(merged_dict.values()))

        # print(merged_data)
        # return
    except Exception as ex:
        print(f"str342__{ex}")

    try:
        if resPhoto != None and resPhoto != []:
            print(f"len_photos___{len(resPhoto)}")
            try:
                with open(f'result_photos__interval_{n1}__{n2}__Items_{len(resPhoto)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resPhoto, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str210__{ex}")
        if resDescription != None and resDescription != []:
            print(f"len_resDescription ___{len(resDescription)}")
            try:
                with open(f'result_description__interval_{n1}__{n2}__Items_{len(resDescription)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resDescription, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"writerr__str86__{ex}") 

        if resFacilities != None and resFacilities != []:
            print(f"len_resFacilities___{len(resFacilities)}")
            try:
                with open(f'result_facilities___interval_{n1}__{n2}__Items_{len(resFacilities)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resFacilities, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}") 
        if resRooms != None and resRooms != []:
            print(f"len_resRooms___{len(resRooms)}")
            try:
                with open(f'result_room__interval_{n1}__{n2}__Items_{len(resRooms)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resRooms, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}")

        if resRoomsBlock != None and resRoomsBlock != []:
            print(f"len_resRoomsBlock___{len(resRoomsBlock)}")
            try:
                with open(f'result_room_block__interval_{n1}__{n2}__Items_{len(resRoomsBlock)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resRoomsBlock, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str221__{ex}") 

        # if resRoomHighlights != None and resRoomHighlights != []:
        #     print(f"len_resRoomHighlights___{len(resRoomHighlights)}")
        #     try:
        #         with open(f'result_room_Highlights_upz_7.json', "w", encoding="utf-8") as file: 
        #             json.dump(resRoomHighlights, file, indent=4, ensure_ascii=False)
        #     except Exception as ex:
        #         print(f"str221__{ex}") 

        if resWhiteList != None and resWhiteList != []:
            print(f"len_resBlackList___{len(resWhiteList)}")
            try:
                with open(f'white_list__interval_{n1}__{n2}__Items_{len(resWhiteList)}.json', "w", encoding="utf-8") as file: 
                    json.dump(resWhiteList, file, indent=4, ensure_ascii=False)
            except Exception as ex:
                print(f"str226__{ex}") 

        # if new_resBlackList != None and new_resBlackList != []:
        #     print(f"len_resBlackList___{len(new_resBlackList)}")
        #     try:
        #         with open(f'black_list_1.json', "w", encoding="utf-8") as file: 
        #             json.dump(new_resBlackList, file, indent=4, ensure_ascii=False)
        #     except Exception as ex:
        #         print(f"str226__{ex}")

    except Exception as ex:
        print(f"writerr__str136__{ex}")

# total = 'jdfkjfdjkdfkj'
# writerr(total)
# python writerr.py


# we have:
# data = [
#     {"id": 1, "url": '1', "f": "0"},
#     {"id": 2, "url": '2', "r": "B"},
#     {"id": 1, "url": '1', "fac": "C"},
#     {"id": 3, "url": '3', "r_b": "D"},
#     {"id": 2, "url": '2', "d": "E"}
# ]

# i want to get:

# new_data = [
#     {"id": 1, "url": '1', "f": "0", "fac": "C"},
#     {"id": 2, "url": '2', "r": "B", "d": "E"},
#     {"id": 3, "url": '3', "r_b": "D"},

# ]

# write me python code for sorting data list ruling of principles selections of new_data list





# if resRevievs != None and resRevievs != []:
#     print(f"len_resRevievs___{len(resRevievs)}")
#     try:
#         with open(f'result_review_upz_7.json', "w", encoding="utf-8") as file: 
#             json.dump(resRevievs, file, indent=4, ensure_ascii=False)
#     except Exception as ex:
#         print(f"str221__{ex}") 

# i have this:
# [
#     [
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "foto": 0
#         },
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "description": 0
#         },
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "facility": 0
#         },
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "room": 0
#         },
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "room_blocks": 0
#         }
#     ],
#     [the same structure]
# ]
# write me python code for getting this:

# [
#     [
#         {
#             "hotel_id": "4012065",
#             "url": "https://www.booking.com/hotel/uz/barselona-s.html",
#             "foto": 0,
#             "description": 0,
#             "facility": 0,
#             "room": 0,
#             "room_blocks": 0
#         },
#        {another sorted dict like first}
#     ]
# ]




        # id_dict = defaultdict(dict)
        # for d in resBlackList:
        #     id_dict[d["hotel_id"]].update(d)        
        # for k, v in id_dict.items():
        #     new_resBlackList.append(v)
        # print(resBlackList)
        # try:
        #     for d in resBlackList:
        #         found = False
        #         for nd in new_resBlackList:
        #             if d["hotel_id"] == nd["hotel_id"]:
        #                 nd.update(d)
        #                 found = True
        #                 break
        #         if not found:
        #             new_resBlackList.append(d)
        # except Exception as ex:
        #     print(ex)

        # return

