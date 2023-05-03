import json

def data_upz_hotels_func():
    data_upz_hotels_renevate = []
    n1 = 801
    n2 = 811
    with open('upz_hotels.json', 'r') as f:
        data_upz_hotels = json.load(f)[n1:n2]
        for item in data_upz_hotels:
            data_upz_hotels_renevate.append(
                { 
                "id": item["id"],    
                "hotel_id": item["hotel_id"],
                "url": item["url"],
                "facility": item["facility"],
                "room": item["room"],
                "fotos": item["fotos"],
                "description": item["description"],
                "otziv": item["otziv"],
                }
            )

        return data_upz_hotels_renevate


# python json_reader_test.py
