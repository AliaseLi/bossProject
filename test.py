import json
from urllib import parse

from db import DB

# 测试数据库
#db_ = DB()


# # 测试城市信息
# with open('city.json', 'rb') as f:
#     data = f.read().decode()
# # print(type(data))
# # print(type(jsonObj))
# citys = json.loads(data)['data']['cityList']
# allCity = {}
# for city in citys:
#     for sub_city in city.get('subLevelModelList'):
#         allCity[sub_city['name']] = sub_city['code']
# print(allCity)

qCity, query = input('请输入需要获取的城市名和岗位名称：(北京-python)').strip().split('-')
print(qCity)
print(query)
params = {
    'query':query
}
query = parse.urlencode(params)
print(query)
start_url = 'https://www.zhipin.com/c{0}/h_{0}/?{1}&page=1'.format(qCity, query)
print(start_url)