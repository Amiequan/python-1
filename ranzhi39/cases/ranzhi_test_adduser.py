import csv
import unittest
from base.ranzhi_driver import RanzhiDriver
from pages.ranzhi_adduser_page import RanzhiAdduserPage
from pages.ranzhi_login_page import RanzhiLoginPage


class RanzhiTestAdduser(unittest.TestCase):
    def setUp(self):
        self.driver = RanzhiDriver('Firefox')
        # self.driver.navigate('http://192.168.1.84/ranzhi/www')#虚拟机网址
        self.driver.navigate('http://localhost/ranzhi/www')
        self.driver.implicitly_wait(1)
        ranzhilogin = RanzhiLoginPage(self.driver)
        ranzhilogin.login_inherit('admin','123456')
        self.driver.sleep(1)

    def tearDown(self):
        self.driver.close_browser()
        # pass

    def test_adduser(self):
        #读取文件
        csv_file = open(r'C:\Users\hzpower\PycharmProjects\ranzhi39'
                        r'\data\adduser.csv','r',encoding='utf8')
        csv_data = csv.reader(csv_file)
        #过滤标题
        is_headle = True
        for line in csv_data:
            if is_headle:
                is_headle = False
                continue
        #创建一个字典
            data={'name':line[0],
                 'realname':line[1],
                 'sex':line[2],
                  'dept': line[3],
                  'role': line[4],
                  'password1': line[5],
                  'password2': line[6],
                  'email': line[7],
                  'casetype': line[8],
                  'exception': line[9]} #注意字典里的字段要一致，否则会出现KeyError
            ranzhilogin = RanzhiAdduserPage(self.driver)
            ranzhilogin.adduser(data)
            if data['casetype'] == '成功':
                url = ranzhilogin.ADDUSER_URL
                self.assertEqual('http://localhost/ranzhi/www/sys/user-admin.html',
                                 url,'添加成员成功')
            if data['casetype'] == '用户名错误':
                name = ranzhilogin.nametext
                self.assertIn('用户名不能为空。;用户名应当为字母或数字的组合，至少三位',
                              name,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '用户名错误1':
                name = ranzhilogin.nametext
                self.assertIn('用户名应当为字母或数字的组合，至少三位',
                              name,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '用户名错误2':
                name = ranzhilogin.nametext
                self.assertIn('用户名已经有zzz这条记录了。',
                              name,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '用户名错误3':
                name = ranzhilogin.nametext
                self.assertIn('用户名长度应当不超过30，且不小于0。',
                              name,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '姓名错误':
                realname = ranzhilogin.realnametext
                self.assertIn('真实姓名不能为空。',
                              realname,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '角色名错误':
                role = ranzhilogin.roletext
                self.assertIn('角色不能为空。',
                              role,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '密码错误':
                pwd = ranzhilogin.pwd1text
                self.assertNotIn('请输入密码;两次密码应当相等。password1不能为空。',
                              pwd,'无效测试用例失败，预期为：'+data['exception'])
            if data['casetype'] == '邮箱错误':
                email = ranzhilogin.emailtext
                self.assertIn('邮箱不能为空。;邮箱应当为合法的EMAIL。;邮箱已经有这条记录了。',
                              email, '无效测试用例失败，预期为：' + data['exception'])
            if data['casetype'] == '邮箱错误1':
                email = ranzhilogin.emailtext
                self.assertIn('邮箱已经有4@126.com这条记录了。',
                              email, '无效测试用例失败，预期为：' + data['exception'])
            if data['casetype'] == '邮箱错误2':
                email = ranzhilogin.emailtext
                self.assertIn('邮箱长度应当不超过90，且不小于0。;邮箱应当为合法的EMAIL。',
                              email, '无效测试用例失败，预期为：' + data['exception'])
            if data['casetype'] == '邮箱错误3':
                email = ranzhilogin.emailtext
                self.assertIn('邮箱应当为合法的EMAIL。',
                              email, '无效测试用例失败，预期为：' + data['exception'])
        csv_file.close()

if __name__ == '__main__':
    unittest.main()

