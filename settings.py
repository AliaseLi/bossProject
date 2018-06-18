# 配置代理服务器
import json
from urllib import parse

proxies = {
    'http':'',
    'https':''
}

def getALLCity():
    # 返回所有城市信息及编码
    with open('city.json', 'rb') as f:
        data = f.read().decode()
    citys = json.loads(data)['data']['cityList']
    allCity = {}
    for city in citys:
        for sub_city in city.get('subLevelModelList'):
            allCity[sub_city['name']] = sub_city['code']
    return allCity

# 配置爬虫起始页
def startUrl(qCity, query):
    allCity = getALLCity()
    qCity_code = allCity.get(qCity)
    query = parse.urlencode({'query': query})
    if not qCity_code:
        qCity_code = allCity.get('北京')
    start_url = 'https://www.zhipin.com/c{0}/h_{0}/?{1}&page=1'.format(qCity_code, query)
    return start_url


# 配置请求头
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:60.0) Gecko/20100101 Firefox/60.0',
}

# 配置数据库（mysql）
DATABASE = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '',
    'db': 'boss',
    'charset': 'utf8'
}


