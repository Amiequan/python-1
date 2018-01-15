import csv
import unittest
from base.ranzhi_driver import RanzhiDriver
from pages.ranzhi_login_page import RanzhiLoginPage

class RanzhiTestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = RanzhiDriver('Firefox')
        # self.driver = RanzhiDriver('Chrome')  #会闪退
        # self.driver.navigate('http://192.168.1.84/ranzhi/www')
        self.driver.navigate('http://localhost/ranzhi/www')
        # self.driver.maximize_window() #启用会报错
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test_login(self):
        #读取文件
        csv_file = open(r'C:\Users\hzpower\PycharmProjects\ranzhi39\data\login.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        #过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
        #创建一个字典
            data = {'name':line[0],
                 'password':line[1],
                 'casetype':line[2]}
            ranzhilogin = RanzhiLoginPage(self.driver)
            ranzhilogin.login(data)
            if data['casetype'] == '登陆失败':
                text = ranzhilogin.LOGIN_TEXT   # 注意流程
                self.assertEqual('登陆 - 然之协同',text,'登陆失败')
            if data['casetype'] == '登陆成功':
                title = ranzhilogin.LOGIN_TITLE
                self.assertEqual('然之协同',title,'登陆成功')
        csv_file.close()

        # sqldata = self.driver.get_sql_data('..\\data\\login.sql','utf8','localhost','ranzhi','utf8')
        # for line in sqldata:
        #     data = {
        #         'name': line[2],
        #         'pwd': line[3]
        #     }
        #     ranzhilogin = RanzhiLoginPage(self.driver)
        #     ranzhilogin.login_inherit_sql(data)
        # self.driver.close_sql()


if __name__ == '__main__':
    unittest.main()

