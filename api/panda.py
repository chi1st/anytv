from bs4 import BeautifulSoup
import requests
import json
# import pymongo
from api import anytv_info
# from model_sqlite import ItemInfo

# con = pymongo.MongoClient('localhost', 27017)
# anytv = con['anytv']
# anytv_info = anytv['anytv_info']
#

def get_data(url):
    wb_data = requests.get(url)
    j = wb_data.text
    # print(type(j))
    # print(j)
    ej = json.loads(j)
    # print(ej)
    # print(type(ej))
    # for i in ej['data']:
    #     print(i.items)
    a = ej['data']['items']
    for i in a:
        # print(i)
        person_num = int(i['person_num'])
        title = i['name']
        url = 'http://www.panda.tv/' + i['id']
        anchor = i['userinfo']['nickName']
        img_url = i['pictures']['img']
        img_name = '熊猫' + i['id'] + '.jpg'
        cate = i['classification']['cname']
        # data_from = '熊猫'
        data = {
            'url': url,
            'data_from': '熊猫',
            'title': title,
            'anchor': anchor,
            'cate': cate,
            'person_num': person_num,
            'img_name': img_name,
            'img_url': img_url
        }
        # print(data)
        anytv_info.insert(data)
        # info = ItemInfo(title, url, person_num, cate, anchor, data_from, img_name, img_url) # sqlite数据库
        # info.save()
    return a


def get_url(page, cate):
    url = 'http://www.panda.tv/ajax_sort?token=&pageno={}&pagenum=120&classification={}'.format(page, cate)
    return url

def get_all_panda_data(cate):
    for c in cate:
        page = 1
        while True:
            cate = c
            url = get_url(page, cate)
            page += 1
            print(page)
            print(url)
            if get_data(url) == []:
                break

panda_cate = ['lol', 'overwatch', 'hearthstone', 'hwzb']

if __name__ == "__main__":
    get_all_panda_data(panda_cate)
    # for c in cate:
    #     page = 1
    #     while True:
    #         cate = c
    #         url = get_url(page, cate)
    #         page += 1
    #         print(url)
    #         if get_data(url) == []:
    #             break

# con.drop_database(pandatv)
