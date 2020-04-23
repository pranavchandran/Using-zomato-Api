# Zomato_api.py

import requests
import json

headers = {'user-key': '260f4f881b2bc2ffbaeae6ada7ac1148',
           'Accept': 'application/json'}


# "https://developers.zomato.com/api/v2.1/cities

def Get_Location_details(location_name):
    data = {'query':location_name}
    url = 'https://developers.zomato.com/api/v2.1/locations'
    data = requests.post(url, headers=headers, params=data)
    data = json.loads(data.text)

    # for keys,values in data.items():
    #     print(f'Keys : {keys} and values : {values}/n')

    # a = data['location_suggestions']
    # print(a)

Get_Location_details('kochi')

def Get_search_Restaurants(entity_id,entity_type,lat,lon,radius,count):
    url = "https://developers.zomato.com/api/v2.1/search"
    data = {'entity_id':entity_id,'entity_type':entity_type,'lat':lat,'lon':lon,'radius':radius,'count':count}
    data = requests.post(url, headers=headers, params=data)
    data = json.loads(data.text)



    # restaurants=[]
    
    # if(len(data["restaurants"])<10):
    #     restoDataLen=len(data["restaurants"])
    # else:
    #     restoDataLen=10

    # print(data)

    for i in range(0, count):
        item={}
        photos=[]
        item["id"]=data["restaurants"][i]["restaurant"]["id"]
        item["name"]=data["restaurants"][i]["restaurant"]["name"]
        # item["url"]=data["restaurants"][i]["restaurant"]["url"]
        item["timings"]=data["restaurants"][i]["restaurant"]["timings"]
        item["votes"]=data["restaurants"][i]["restaurant"]["user_rating"]["votes"]
        item["ratings"]=data["restaurants"][i]["restaurant"]["user_rating"]["aggregate_rating"]
        item["price_range"]=data["restaurants"][i]["restaurant"]["price_range"]
        item["location"]=data["restaurants"][i]["restaurant"]["location"]["locality_verbose"]
        item["zipcode"]=data["restaurants"][i]["restaurant"]["location"]["zipcode"]
        

        print(item,'\n')


    

Get_search_Restaurants(9,'city',9.97,76.28,500,10)