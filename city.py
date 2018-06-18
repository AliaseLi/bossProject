# 获取boss直聘所有城市信息
from urllib import request

import settings

url = 'https://www.zhipin.com/common/data/city.json'

req = request.Request(url, headers=settings.headers)
resp = request.urlopen(req)
if resp.status == 200:
    print('请求成功')
    jsonData = resp.read()
    with open('city.json','wb') as f:
        f.write(jsonData)
    print('保存city.json 成功')