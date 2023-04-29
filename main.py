import requests as r
import time as t
import urllib.parse as u
import datetime
import os
token = os.environ["token"]
txt="""

六分钟一言：.hitokoto.

现在的微博热搜榜三：#.weibotop.#

北京天气：.bjwe.

更新时间（UTC）：.date.

B站榜一：

![](bilibili:.bilibili.)

动态主页支持请私信。OIso订阅者支持免费代部署。
"""
cookies={"__client_id":token,"_uid":"395758"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47 BOTE"}
txt=txt.replace(".weibotop.","["+r.get("https://tenapi.cn/v2/weibohot").text.split('"name": "')[1].split('",')[0]+"]("+r.get("https://tenapi.cn/v2/weibohot").text.split('"url": "')[1].split('"')[0]+")")
txt=txt.replace(".weibotop3.",r.get("https://tenapi.cn/v2/weibohot").text.split('"name": "')[3].split('",')[0])
txt=txt.replace(".date.",str(datetime.datetime.today()))
txt=txt.replace(".bilibili.","av"+r.get("https://api.bilibili.com/x/web-interface/ranking/v2").text.split('"aid":')[1].split(',"videos"')[0])
txt=txt.replace(".hitokoto.",r.get("https://v1.hitokoto.cn/").text.split('"hitokoto":"')[1].split('","typ')[0])
txt=txt.replace(".bjwe.",r.get("http://t.weather.itboy.net/api/weather/city/101010100").text.split('"type":"')[1].split('","n')[0])
first=r.get("https://v1.hitokoto.cn/").text.split('"hitokoto":"')[1].split('","typ')[0]
re=r.get("https://www.luogu.com.cn/user/395758",headers=headers,cookies=cookies)
headers["X-CSRF-TOKEN"]=re.text.split('name="csrf-token" content="')[1].split('">\n')[0]
headers["Referer"]="https://www.luogu.com.cn/user/395758"
re=r.post("https://www.luogu.com.cn/api/user/updateIntroduction",json={"introduction":txt},headers=headers,cookies=cookies)
print(re)
re=r.post("https://www.luogu.com.cn/api/user/updateSlogan",json={"slogan":first},headers=headers,cookies=cookies)
print(re)
