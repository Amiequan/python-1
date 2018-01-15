import unittest
from base.uckefu_driver import UCKeFuDriver
from pages.uckefu_login_page import UCKeFuLoginPage
from pages.uckefu_servicetagmg_page import UCKeFUSetservicetagPage


class UCKeFUSetService(unittest.TestCase):
    def setUp(self):
        self.driver = UCKeFuDriver('Firefox')
        self.driver.navigate("http://localhost:8080/")
        # self.driver.navigate("http://192.168.1.111:8080")
        self.driver.implicitly_wait(3)
        login = UCKeFuLoginPage(self.driver)
        login.logininherit('admin','123456')
        self.driver.sleep(3)

    def tearDown(self):
        # self.driver.close_browser()
        pass

    def test_uckefu_setservice(self):
        csv_data = self.driver.get_csv_data('..\\data\\setservicetagmg.csv','utf8')
        # 过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
            # 创建一个字典
            data = {'tagmg':line[0],
                    'name':line[1],
                    'color':line[2]}
            setservicetag = UCKeFUSetservicetagPage(self.driver)
            setservicetag.setservicetag(data)
        self.driver.close_csv_file()

if __name__ == '__main__':
    unittest.main()