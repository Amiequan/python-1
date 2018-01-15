import csv
import unittest
from base.ranzhi_driver import RanzhiDriver
from pages.ranzhi_docs import RanzhiDocsPage
from pages.ranzhi_login_page import RanzhiLoginPage

class RanzhiTestDocs(unittest.TestCase):
    def setUp(self):
        self.driver = RanzhiDriver('Firefox')
        # self.driver.navigate('http://192.168.1.84/ranzhi/www')
        self.driver.navigate('http://localhost/ranzhi/www')
        # self.driver.maximize_window()#报错
        self.driver.implicitly_wait(1)
        ranzhilogin = RanzhiLoginPage(self.driver)
        ranzhilogin.login_inherit('admin','123456')
        self.driver.sleep(1)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test1_docs(self):
        #读取文件
        csv_file = open(r'C:\Users\hzpower\PycharmProjects\ranzhi39\data\docs.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        #过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
        #创建一个字典
            data={'libtype':line[0],
                  'name':line[1],
                 'username':line[2],
                 'group':line[3]} #注意字典里的字段要一致，否则会出现KeyError
            ranzhidocs = RanzhiDocsPage(self.driver)
            ranzhidocs.docs(data)
        csv_file.close()

    def test2_adddoc(self):
            # 读取文件
            csv_file = open(r'C:\Users\hzpower\PycharmProjects\ranzhi39\data\adddoc.csv', 'r', encoding='utf8')
            csv_data = csv.reader(csv_file)
            # 过滤标题
            is_headle = True
            for line in csv_data:
                if is_headle:
                    is_headle = False
                    continue
                    # 创建一个字典
                data = {'module':line[0],
                    'username': line[1],
                        'group': line[2],
                        'type': line[3],
                        'title': line[4],
                        'body': line[5],
                        'key': line[6]}  # 注意字典里的字段要一致，否则会出现KeyError
                ranzhiadddoc = RanzhiDocsPage(self.driver)
                ranzhiadddoc.adddoc(data)
            csv_file.close()

if __name__ == '__main__':
    unittest.main()