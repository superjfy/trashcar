# -*- coding: utf-8 -*
import requests
import json

token = "URcWh4jqXmWSxmpiPoraXBDeTXu0WWcFO0fFMkIdyHp"


def lineNotify(token, msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code


req = requests.get("https://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json")
data_dict = json.loads(req.text)
city_len = len(data_dict)
for i in range(city_len):
    city_now = data_dict[i]["cityname"]
    car_plat = data_dict[i]["car"]
    data_time = data_dict[i]["time"]
    if city_now == u"新莊區":
        if u"銘德街" in data_dict[i]["location"]:
            msg = data_dict[i]["location"]
            lineNotify(token, msg)


