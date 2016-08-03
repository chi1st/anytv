import requests
import json
from api import proxy_list
import random
from api import anytv_info


def get_data(url):
    global proxy_list
    proxies = random.choice(proxy_list) # 随机获取代理ip
    wb_data = requests.get(url, proxies=proxies)
    j = wb_data.text
    # print(type(j))
    # print(j)
    ej = json.loads(j)
    # print(ej)
    # print(type(ej))
    # for i in ej['data']:
    # print(i.items)
    a = ej['data']['list']
    # print(a)
    # print(type(a))
    print(url)
    for i in a:
        person_num = int(i['totalCount'])
        title = i['introduction']
        url = 'http://www.huya.com/' + i['privateHost']
        anchor = i['nick']
        img_url = i['screenshot']
        img_name = '虎牙' + i['privateHost'] + '.jpg'
        cate = i['gameFullName']
        data = {
            'url': url,
            'data_from': '虎牙',
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


def get_url(page, cate):
    url = 'http://www.huya.com/index.php?m=Game&do=ajaxGameLiveByPage&gid={cate}&page={page}'.format(page=page,
                                                                                                     cate=cate)
    return url


huya_cate = ['1', '2174', '393', '2165']

def get_all_huya_data(cate):
    for c in cate:
        page = 1
        while True:
            cate = c
            url = get_url(page, cate)
            print(page)
            page += 1
            # print(url)
            if get_data(url) == []:
                break

# if __name__ == "__main__":
#                 get_all_huya_data(huya_cate)
    # for c in cate:
    #     page = 1
    #     while True:
    #         cate = c
    #         url = get_url(page, cate)
    #         print(page)
    #         page += 1
    #         print(url)
    #         if get_data(url) == []:
    #             break
