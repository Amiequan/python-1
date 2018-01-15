import unittest
from base.uckefu_driver import UCKeFuDriver
from pages.uckefu_login_page import UCKeFuLoginPage


class UCKeFuTestLogin(unittest.TestCase):
    login_url = "http://localhost:8080/"
    # login_url = "http://192.168.1.111:8080/"

    def setUp(self):
        # self.driver = UCKeFuDriver('Firefox')
        self.driver = UCKeFuDriver('Chrome')
        self.driver.maximize_window()  # 居然闪退
        self.driver.navigate(self.login_url)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def uckefu_test_login(self):
        csv_data = self.driver.get_csv_data('C:\\Users\\hzpower\\PycharmProjects'
                                            '\\UCKeFu\\data\\login.csv', 'utf8')
        # 过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
            # 创建一个字典
            data = {'name': line[0],
                    'pwd': line[1],
                    'casetype': line[2]}
            uckefulogin = UCKeFuLoginPage(self.driver)
            uckefulogin.login(data)
            # if data['casetype'] == '登录成功':
            #     self.assertEqual('http://localhost:8080/',self.driver.url,'登录成功')
            # if data['casetype'] == '登录失败':
            #     self.assertEqual('http://localhost:8080/',self.driver.url,'登录失败')
            # if data['casetype'] == '登录失败1':
            try:
                text = uckefulogin.text
                self.assertEqual('用户名或密码错误，请重新填写', text,'登录失败')
                print('try')
            except:
                self.driver.get_screenshot('C:\\Users\\hzpower\\PycharmProjects\\UCKeFu\\screenshots')
                print('except')
                raise
        self.driver.close_csv_file()


if __name__ == '__main__':
    unittest.main()