import requests
import json
import random
from api import anytv_info
from api import proxy_list


def get_data(url):
    global proxy_list
    proxies = random.choice(proxy_list)# 随机获取代理ip
    wb_data = requests.get(url, proxies=proxies)
    j = wb_data.text
    # print('j', j)
    # print(type(j))
    # print(j)
    ej = json.loads(j)
    # print('ej', ej)
    # print(ej)
    # print(type(ej))
    # for i in ej['data']:
    #     print(i.items)
    a = ej['data']
    # print(a)
    for i in a:
        # print(i)
        person_num = int(i['view'])
        title = i['title']
        url = 'http://www.quanmin.tv/v/' + i['uid']
        anchor = i['nick']
        img_url = i['thumb']
        img_name = '全民' + i['uid'] + '.jpg'
        cate = i['category_name']
        data = {
            'url': url,
            'data_from': '全民',
            'title': title,
            'anchor': anchor,
            'cate': cate,
            'person_num': person_num,
            'img_name': img_name,
            'img_url': img_url
        }
        # print(data)
        anytv_info.insert(data)
    return a

def get_url(page,cate):
    if page == 0:
        url = 'http://www.quanmin.tv/json/categories/{cate}/list.json'.format(cate=cate)
    else:
        url = 'http://www.quanmin.tv/json/categories/{cate}/list_{page}.json'.format(page=page, cate=cate)
    return url

quanming_cate = ['lol', 'overwatch', 'heartstone', 'huwai']

def get_all_quanming_data(cate):
    for c in cate:
        page = 0
        while True:
            cate = c
            print(page)
            url = get_url(page, cate)
            print(url)
            page += 1
            try:
                if get_data(url) == []:
                    break
            except:
                break



# if __name__ == "__main__":
#     get_all_quanming_data(quanming_cate)

