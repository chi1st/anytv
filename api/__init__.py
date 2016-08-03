import requests
import pymongo
import json
resp = requests.get("http://tor1024.com/static/proxy_pool.txt")
ips_txt = resp.text.strip().split("\n")
proxy_list = []
for i in ips_txt:
    try:
        k = json.loads(i)
        proxy_list.append(k)
    except Exception as e:
        print(e)

con = pymongo.MongoClient('localhost', 27017)
anytv = con['anytv']
TV = con['TV']
anytv_info = anytv['anytv_info']