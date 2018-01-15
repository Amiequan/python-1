from base.base_page import RanzhiBasePage
from base.log import Log


class RanzhiLoginPage(RanzhiBasePage):
    LOGIN_USER ='account'
    LOGIN_PWD ='password'
    LOGIN_BUTTON ='submit'
    LOGINOUT_BUTTON ='l,签退'
    LOGIN_BUTTON_DISMISS ='x,/html/body/div[2]/div/div/div[1]/div'

    def login(self, data):
        '''测试登陆'''
        # 通过base_driver获取RanzhiDriver里面的driver
        driver =self.base_driver
        #休眠等待
        driver.sleep(1)
        #输入用户名密码
        log = Log('logs')
        log.info('输入用户名')
        driver.type1(self.LOGIN_USER,data['name'])
        log.info('输入密码')
        driver.type1(self.LOGIN_PWD,data['password'])
        #点击登录
        log.info('登录然之协同')
        driver.click(self.LOGIN_BUTTON)
        #休眠等待
        driver.sleep(1)
        if data['casetype'] =='登陆成功':
            log.info('登录成功后获取页面标题')
            self.LOGIN_TITLE = driver.get_title()
            print(self.LOGIN_TITLE)
            log.info('点击签退')
            driver.click(self.LOGINOUT_BUTTON)
            driver.sleep(1)
        if data['casetype'] =='登陆失败':
            log.info('登录失败后获取错误提示信息')
            self.LOGIN_TEXT = driver.get_text()
            print(self.LOGIN_TEXT)
            log.info('点击确定按钮')
            driver.click(self.LOGIN_BUTTON_DISMISS)
            driver.sleep(1)

    def login_inherit(self,name,pwd):
        '''正常登陆'''
        driver =self.base_driver
        #休眠等待
        driver.sleep(1)
        #输入用户名密码
        driver.type1(self.LOGIN_USER,name)
        driver.type1(self.LOGIN_PWD,pwd)
        #点击登录
        driver.click(self.LOGIN_BUTTON)
        #休眠等待
        driver.sleep(1)

    def login_inherit_sql(self,data):
        '''正常登陆'''
        driver =self.base_driver
        #休眠等待
        driver.sleep(1)
        #输入用户名密码
        driver.type1(self.LOGIN_USER,data['name'])
        driver.type1(self.LOGIN_PWD,data['pwd'])
        #点击登录
        driver.click(self.LOGIN_BUTTON)
        #休眠等待
        driver.sleep(1)


