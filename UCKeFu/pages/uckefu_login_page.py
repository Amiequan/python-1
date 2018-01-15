from base.base_page import BasePage


class UCKeFuLoginPage(BasePage):
    login_tooltip1 = "x,.//*[@id='ukefu-cousult-invite-dialog']/a/span"
    login_tooltip2 = "x,html/body/div[1]/div[1]/div/ul/li[4]/a"
    login_name = "username"
    login_pwd = "name,password"
    login_boutton = "x,.//*[@id='loginForm']/div[5]/div/button"
    text = "x,.//*[@id='layui-layer1']/div[2]"
    login_tipbotton = "x,.//*[@id='layui-layer1']/div[3]/a"
    login_out = "x,html/body/div[1]/div[1]/div/ul/li[4]/a"
    loginout = "l,退出系统"

    def login(self, data):
        '''测试登录UCKeFu系统'''
        driver = self.base_driver
        self.log('点击关闭邀请框')
        driver.click(self.login_tooltip1)
        driver.sleep(5)
        self.log('输入用户名')
        driver.type2(self.login_name,data['name'])
        self.log('输入密码')
        driver.type(self.login_pwd,data['pwd'])
        self.log('点击登录')
        driver.click(self.login_boutton)
        driver.sleep(3)
        self.log('刷新当前页面')
        driver.refresh()
        if data['casetype'] == '登录成功':
            self.log('登录成功')
            self.log('获取当前页面url')
            self.url = driver.get_url()
            # 移动到系统管理员
            driver.move_to(self.login_out)
            driver.click(self.login_out)
            driver.sleep(5)
            # 点击退出系统
            driver.move_to(self.loginout)
            driver.sleep(1)
            self.log('退出系统')
            driver.click(self.loginout)
            driver.sleep(3)
        if data['casetype'] == '登录失败':
            self.log('登录失败')
            self.log('获取当前页面url')
            self.url = driver.get_url()
            driver.sleep(3)
        if data['casetype'] == '登录失败1':
            self.log('获取登录失败提示信息')
            self.text = driver.get_text(self.text)
            self.log('错误信息,点击确认')
            driver.click(self.login_tipbotton)
            driver.sleep(3)

    def logininherit(self,name,pwd):
        '''成功登录UCKeFu系统'''
        driver = self.base_driver
        driver.refresh()
        self.log('关闭邀请提示框信息')
        driver.click(self.login_tooltip1)
        self.log('输入用户名')
        driver.type2(self.login_name, name)
        self.log('输入密码')
        driver.type2(self.login_pwd, pwd)
        self.log('点击登录')
        driver.click(self.login_boutton)

