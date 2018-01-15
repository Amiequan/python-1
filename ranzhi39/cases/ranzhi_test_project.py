import csv
import unittest
from base.ranzhi_driver import RanzhiDriver
from pages.ranzhi_login_page import RanzhiLoginPage
from pages.ranzhi_project import RanzhiProjectPage

class RanzhiTestProject(unittest.TestCase):
    def setUp(self):
        self.driver = RanzhiDriver('Firefox')
        # self.driver = RanzhiDriver('Chrome')
        # self.driver.navigate('http://192.168.1.84/ranzhi/www')#虚拟机网址
        self.driver.navigate('http://localhost/ranzhi/www')
        # self.driver.maximize_window()#报错
        self.driver.implicitly_wait(1)
        ranzhilogin = RanzhiLoginPage(self.driver)
        ranzhilogin.login_inherit('admin','123456')
        self.driver.sleep(3)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test_adduser(self):
        #读取文件
        csv_file = open(r'C:\Users\hzpower\PycharmProjects\ranzhi39\data\project.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        #过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
        #创建一个字典
            data={'blocks':line[0],
                  'title':line[1],
                 'grid':line[2],
                 'data-id':line[3],
                  'num': line[4]} #注意字典里的字段要一致，否则会出现KeyError
            ranzhiproject = RanzhiProjectPage(self.driver)
            ranzhiproject.project(data)
        csv_file.close()

if __name__ == '__main__':
    unittest.main()

