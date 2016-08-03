from flask import Flask
from flask import render_template
from flask import request

from models import ItemInfo

app = Flask(__name__)


def get_pagination(cate):
    cate = cate
    page = request.args.get('page', 1, type=int)
    if cate in ['英雄联盟', '守望先锋', '炉石传说', '户外直播']:
        query = ItemInfo.objects(cate=cate).order_by('-person_num')
    elif cate in ['虎牙', '斗鱼', '熊猫', '全民']:
        query = ItemInfo.objects(data_from=cate).order_by('-person_num')
    else:
        query = ItemInfo.objects.order_by('-person_num')
    pagination = query.paginate(page=page, per_page=60, error_out=False)
    posts = pagination.items
    return posts, pagination


@app.route('/')
def all():
    cate = '全部直播'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/', db=posts, cate=cate, pagination=pagination)


@app.route('/lol')
def lol():
    cate = '英雄联盟'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/lol', db=posts, cate=cate, pagination=pagination)


@app.route('/overwatch')
def overwatch():
    cate = '守望先锋'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/overwatch', db=posts, cate=cate, pagination=pagination)


@app.route('/hwzb')
def hwzb():
    cate = '户外直播'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/hwzb', db=posts, cate=cate, pagination=pagination)


@app.route('/panda')
def panda():
    cate = '熊猫'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/panda', db=posts, cate=cate, pagination=pagination)


@app.route('/huya')
def huya():
    cate = '虎牙'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/huya', db=posts, cate=cate, pagination=pagination)


@app.route('/douyu')
def douyu():
    cate = '斗鱼'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/douyu', db=posts, cate=cate, pagination=pagination)


@app.route('/quanming')
def quanming():
    cate = '全民'
    posts, pagination = get_pagination(cate)
    return render_template('TV.html', url='/quanming', db=posts, cate=cate, pagination=pagination)


# def get_data():
#     try:
#         con.drop_database(anytv)
#         mul()
#     except:
#         pass

if __name__ == '__main__':
    app.run(port=8080, debug=True)


