# -*- coding: utf-8 -*
import requests
import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

def linebot_msg(lineAccessToken, msg):
    line_bot_api = LineBotApi(lineAccessToken)
    line_bot_api.push_message('C9608ef211aeebf77abedaee292160169', TextSendMessage(text=msg))

def lineNotify(token, msg):
    url = "https://notify-api.line.me/api/notify"
    headers = {
        "Authorization": "Bearer " + token,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    payload = {'message': msg}
    r = requests.post(url, headers=headers, params=payload)
    return r.status_code

lineAccessToken = "yLbk5g3LkoCwqPpKkaRkI9S0DPZ871Z/tQg4KQRLl1G55j07EzjyJzW8ad2MTWDUp8VZ+NSvpdCSH/QarP5ju/t7/1AfdCOBNCp+rNbXjWUkm1R1Kln/BK4JNVOVQ+y981rgYb3dg8nuA0baLY9sRAdB04t89/1O/w1cDnyilFU="
channelSecret = "5bb12c08aa3a7b6836c3039472cf23e6"
token = "URcWh4jqXmWSxmpiPoraXBDeTXu0WWcFO0fFMkIdyHp"
req = requests.get("https://data.ntpc.gov.tw/od/data/api/28AB4122-60E1-4065-98E5-ABCCB69AACA6?$format=json")
data_dict = json.loads(req.text)
city_len = len(data_dict)
for i in range(city_len):
    city_now = data_dict[i]["cityname"]
    car_plat = data_dict[i]["car"]
    data_time = data_dict[i]["time"]
    if city_now == u"新莊區":
        if u"銘德街" in data_dict[i]["location"]:
            msg = u"垃圾車位置:{}".format(data_dict[i]["location"])
            #lineNotify(token, msg)
            linebot_msg(lineAccessToken, msg)