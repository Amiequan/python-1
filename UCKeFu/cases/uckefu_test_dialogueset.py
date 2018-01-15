import csv
import unittest
from base.uckefu_driver import UCKeFuDriver
from pages.uckefu_login_page import UCKeFuLoginPage
from pages.uckefu_dialogueset_page import UCKeFUDialoguesetPage

class UCKeFUSetService(unittest.TestCase):
    def setUp(self):
        self.driver = UCKeFuDriver('Firefox')
        self.driver.navigate("http://localhost:8080")
        # self.driver.navigate("http://192.168.1.111:8080/")
        self.driver.implicitly_wait(3)
        login = UCKeFuLoginPage(self.driver)
        login.logininherit('admin','123456')
        self.driver.sleep(3)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test_uckefu_setservice(self):
        csv_file = open('C:\\Users\\hzpower\\PycharmProjects\\UCKeFu\\data\\dialogueset.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        # 过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
            # 创建一个字典
            data = {'welcomemsg':line[0],
                    'noagentmsg':line[1],
                    'busymsg':line[2],
                    'successmsg':line[3],
                    'finessmsg':line[4],
                    'policy':line[5],
                    'maxnum':line[6],
                    'readynum':line[7],
                    'timeout':line[8],
                    'timeoutmsg':line[9],
                    'retimeout':line[10],
                    'retimeoutmsg':line[11],
                    'agenttimeout':line[12],
                    'agenttimeoutmsg':line[13],
                    'hour':line[14],
                    'minute':line[15],
                    'rehour':line[16],
                    'reminute':line[17],
                    'hourchecktip':line[18]}
            dialogueset = UCKeFUDialoguesetPage(self.driver)
            dialogueset.dialogueset(data)
        csv_file.close()

if __name__ == '__main__':
    unittest.main()