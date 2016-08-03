from bs4 import BeautifulSoup
import requests
from api import anytv_info

# con = pymongo.MongoClient('localhost', 27017)
# anytv = con['anytv']
# anytv_info = anytv['anytv_info']


# proxies = random.choice(proxy_list) # 随机获取代理ip
# http://www.douyu.com/directory/game/LOL?page=1&isAjax=1
# http://www.douyu.com/directory/game/LOL?page=2&isAjax=1
# http://www.douyu.com/directory/game/LOL?page=9&isAjax=1
# resp = requests.get("http://tor1024.com/static/proxy_pool.txt")
# ips_txt = resp.text.strip().split("\n")
# proxy_list = []
# for i in ips_txt:
#     try:
#         k = json.loads(i)
#         proxy_list.append(k)
#     except Exception as e:
#         print(e)
def get_url(page, cate):
    url = 'http://www.douyu.com/directory/game/{cate}?page={page}'.format(page=page, cate=cate)
    return url


def get_data(url, name_list):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')

    # print(soup)
    titles = soup.select('#live-list-contentbox > li > a > div > div > h3')
    # print(titles)
    anchors = soup.select('span.dy-name.ellipsis.fl')
    # print(anchors)
    cates = soup.select('#live-list-contentbox > li > a > div > div > span')
    # print(cates)
    urls = soup.select('#live-list-contentbox > li > a')
    # print(urls)
    person_nums = soup.select('#live-list-contentbox > li > a > div > p > span.dy-num.fr')

    # print(person_nums)
    img_urls = soup.select('#live-list-contentbox > li > a > span > img')
    a = zip(titles, anchors, cates, urls, person_nums, img_urls)
    # data = []
    r = {'success': '继续'}
    for title, anchor, cate, url, person_num, img_url in a:
        # print(title)
        # print(anchor)
        # print(cate)
        # print(url.get('href'))
        # print(person_num)
        # print(img_urls)
        num = str(person_num.text)
        # print(num, type(num))
        if '万' in num:
            num = float(num.split('万')[0]) * 10000
        name = anchor.text
        info = {
            'data_from': '斗鱼',
            'title': title.text,
            'anchor': anchor.text,
            'cate': cate.text,
            'url': 'http://www.douyu.com' + url.get('href'),
            'person_num': int(num),
            'img_name': 'hehe',
            'img_url': img_url.get('data-original')
        }

        # print(info)
        # print(name)
        # print(data.keys())
        # print(name in data)
        # print(name)
        # print(name_list)
        # print(name not in name_list)
        if name not in name_list:
            name_list.append(name)
            # print('继续')
            # data.append(info)
            anytv_info.insert(info)
            # name_list.append(name)
            r['success'] = '继续'
        else:
            # print('页面重复')
            r['success'] = '页面重复'

    # print(r)
    return r


douyu_cate = ['LOL', 'Overwatch', 'How', 'outdoor']


def get_all_douyu_data(cate):
    for c in cate:
        name_list = []
        page = 1
        while True:
            cate = c
            url = get_url(page, cate)
            page += 1
            print(page)
            print(url)
            a = get_data(url, name_list)
            # get_data(url, name_list)
            if a['success'] == '页面重复':
                break

# if __name__ == '__main__':
#     get_all_douyu_data(douyu_cate)
    # for c in cate:
    #     name_list = []
    #     page = 1
    #     while True:
    #         cate = c
    #         url = get_url(page, cate)
    #         page += 1
    #         print(url)
    #         a = get_data(url, name_list)
    #         # get_data(url, name_list)
    #         if a['success'] == '页面重复':
    #             break
