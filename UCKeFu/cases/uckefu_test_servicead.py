import csv
import unittest
from base.uckefu_driver import UCKeFuDriver
from pages.uckefu_login_page import UCKeFuLoginPage
from pages.uckefu_servicead_page import UCKeFUSetserviceadPage

class UCKeFUSetService(unittest.TestCase):
    def setUp(self):
        # self.driver = UCKeFuDriver('Firefox')
        self.driver = UCKeFuDriver('Chrome')
        self.driver.navigate("http://localhost:8080/")
        # self.driver.navigate("http://192.168.1.111:8080")
        self.driver.implicitly_wait(3)
        login = UCKeFuLoginPage(self.driver)
        login.logininherit('admin','123456')
        self.driver.sleep(3)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test_uckefu_setservice(self):
        csv_file = open('C:\\Users\\hzpower\\PycharmProjects\\UCKeFu\\data\\setservicead.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        # 过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
            # 创建一个字典
            data = {'admg':line[0],
                    'name':line[1],
                    'weight':line[2],
                    'adtype':line[3],
                    'hinttext':line[4],
                    'address':line[5],
                    'adtext':line[6]}
            setservicead = UCKeFUSetserviceadPage(self.driver)
            setservicead.setservicead(data)
        csv_file.close()

if __name__ == '__main__':
    unittest.main()