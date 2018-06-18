import json
import ssl
from urllib import request

import time
from bs4 import BeautifulSoup

import settings
from db import DB
from info import Info


class BossSpiser:
    def __init__(self):
        self.db = DB()
        ssl._create_default_https_context=ssl._create_unverified_context
        print('小蜘蛛，走起..')

    def __del__(self):
        print('今天收成不错，收网回家..')
        self.db.close()

    def run(self, qCity, query):
        next_url = settings.startUrl(qCity, query)
        print(next_url)
        while True:
            html = self.request(next_url)
            # print(html)
            next_url = self.parse(html)
            print(next_url)
            if next_url=='https://www.zhipin.comjavascript:;':
                break
            time.sleep(2)

    def request(self, url):
        # 请求网页
        req = request.Request(url,headers=settings.headers)
        resp = request.urlopen(req)
        if resp.status == 200:
            print('ok')
            html = resp.read()
            # with open('boss_sh.html','wb') as f:
            #     f.write(html)
            return html



    def parse(self, html):
        # 解析网页
        soup = BeautifulSoup(html, 'lxml')
        jobs = soup.select('div[class="job-primary"]')
        for job in jobs:
            job_info = job.select('div[class="info-primary"]')[0]
            # print(job_info)
            job_a = job_info.select('a')[0]
            # print(job_a)
            job_detail_href = 'https://www.zhipin.com' + job_a.attrs.get('href')  # 详情
            # print(job_detail_href)
            job_name = job_a.div.get_text()  # 职位名称
            # print(job_name)
            job_salary_region = job_a.span.get_text().replace('k','')  # 薪资范围
            # print(job_salary_region)
            job_summary = list(filter(lambda x: isinstance(x, str), job_info.p.contents))
            city, job_age, edu = job_summary   # 城市，工作年限，学历
            # print(city,job_age,edu)

            company_info = job.select('div[class="company-text"]')[0]
            company_name = company_info.a.text  # 公司名称
            # print(company_name)
            company_summary = list(filter(lambda x: isinstance(x, str), company_info.p.contents))
            if len(company_summary) == 2:
                industry, scale = company_summary  # 行业，规模
                money = ''
                # print(industry,scale)
            else:
                industry, money, scale = company_summary  # 行业，融资，规模
                # print(industry, money, scale)
            # print('--------------------')

            # 创建info对象
            info = Info(job_name,job_salary_region,city,job_age,edu,company_name,industry,money,scale,job_detail_href)
            # print(info)

            self.saveDB(info)


        # 下一页
        next_url = 'https://www.zhipin.com' + soup.select('div[class="page"] a')[-1].get('href')
        return next_url

    def saveDB(self, info):
        # 保存到数据库
        self.db.save(info)




if __name__ == '__main__':
    qCity, query = input('请输入需要获取的城市名和岗位名称：(北京-python)').strip().split('-')
    print(qCity, query)
    BossSpiser().run(qCity, query)