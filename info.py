# 招聘信息类

class Info:
    def __init__(self, job_name, salary, city, job_age, edu, commany, industry, money, scale, href):
        self.scale = scale  # 公司规模
        self.money = money  # 融资情况
        self.industry = industry  # 所属行业
        self.commany = commany  # 公司名称
        self.edu = edu  # 学历要求
        self.job_age = job_age  # 工作经验
        self.city = city  # 城市
        self.salary = salary  # 薪资范围（以千为单位）
        self.job_name = job_name  # 职位名称
        self.href = href  # 链接地址

    def __str__(self):
        return '职位:{}, 薪资:{}, 城市:{}, 工作经验:{}, 学历:{}, 公司名称:{}, 行业:{}, 融资:{}, 规模:{}, 详情:{}'.\
            format(self.job_name, self.salary, self.city, self.job_age, self.edu, self.commany, self.industry, self.money, self.scale, self.href)