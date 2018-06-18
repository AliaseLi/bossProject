import pymysql

import settings


class DB:
    def __init__(self):
        self.db = pymysql.connect(**settings.DATABASE)
        self.cursor = self.db.cursor()
        print('数据库连接成功')

    def save(self, item):
        self.cursor.execute('insert work(job_name, salary, city, job_age, edu, commany, industry, money, scale, href) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                            args=(item.job_name, item.salary, item.city, item.job_age, item.edu, item.commany, item.industry, item.money, item.scale, item.href))
        if self.cursor.rowcount:
            # print('数据保存成功')
            self.db.commit()  # 提交事务

    def close(self):
        self.db.close()   # 关闭数据库连接