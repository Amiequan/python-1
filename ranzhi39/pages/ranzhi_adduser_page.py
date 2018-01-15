from base.base_page import RanzhiBasePage
from base.log import Log

class RanzhiAdduserPage(RanzhiBasePage):
    ADDUSER_HOUITAI = "x,.//*[@id='s-menu-superadmin']/button"
    ADDUSER_FRAME ='iframe-superadmin'
    ADDUSER_ZUZHI = "x,//*[@id='mainNavbar']/ul/li[2]/a"
    ADDUSER_TIANJIA = 'x,html/body/div[1]/div/div/div[1]/div/div[2]/a[1]'
    ADDUSER_NAME ='account'
    ADDUSER_RLNM ='realname'
    SEX_BUTTON ="x,.//*[@id='ajaxForm']/table/tbody/tr[3]/td/label[1]"
    ADDUSER_DEPT ='dept'
    ADDUSER_ROLE ='role'
    ADDUSER_PWD1 ='password1'
    ADDUSER_PWD2 = 'password2'
    ADDUSER_EMAIL ='email'
    BAOCUN_BUTTON ='submit'
    GENDERM_BUTTON ="x,.//*[@id='ajaxForm']/table/tbody/tr[3]/td/label[1]"
    GENDERF_BUTTON ="x,.//*[@id='ajaxForm']/table/tbody/tr[3]/td/label[2]"
    ADDUSER_BUTTON ="x,html/body/div[1]/div/div/div[1]/div/div[2]/a[1]"
    ADDUSER_NAMETEXT ="accountLabel"
    ADDUSER_RLNMTEXT ="realnameLabel"
    ADDUSER_ROLETEXT ="roleLabel"
    ADDUSER_PWD1TEXT ="password1Label"
    ADDUSER_EMAILTEXT ="s,#emailLabel"

    def adduser(self,data):
        driver =self.base_driver
        #休眠等待
        driver.sleep(1)
        #点击后台管理
        log = Log('..\\logs')
        log.info('点击后台管理')
        driver.click(self.ADDUSER_HOUITAI)
        # 点击组织
        log.info('点击组织')
        driver.sleep(2)
        driver.switch_to_frame(self.ADDUSER_FRAME)
        driver.click(self.ADDUSER_ZUZHI)
        #点击添加成员
        log.info('点击添加成员')
        driver.click(self.ADDUSER_TIANJIA)
        #输入用户名，真实姓名
        log.info('输入用户名，真实姓名')
        driver.type(self.ADDUSER_NAME,data['name'])
        driver.type(self.ADDUSER_RLNM,data['realname'])
        #选择性别
        log.info('选择性别')
        if data['sex'] =='男':
            driver.click(self.GENDERM_BUTTON)
        if data['sex'] =='女':
            driver.click(self.GENDERF_BUTTON)
        else:
            pass
        #选择部门，角色
        log.info('选择部门，角色')
        driver.select_by_visible_text(self.ADDUSER_DEPT,data['dept'])
        driver.select_by_value(self.ADDUSER_ROLE,data['role'])
        #输入密码，重复密码，邮箱
        log.info('输入密码，重复密码，邮箱')
        driver.type(self.ADDUSER_PWD1,data['password1'])
        driver.type(self.ADDUSER_PWD2,data['password2'])
        driver.type(self.ADDUSER_EMAIL,data['email'])
        #点击保存
        log.info('点击保存')
        driver.click(self.BAOCUN_BUTTON)
        driver.sleep(1)
        # 获取url
        log.info('获取url')
        self.ADDUSER_URL = driver.get_url()
        try:
            driver.click(self.ADDUSER_URL)
        except Exception as msg:
            driver.get_screenshot('screenshot')
        #获取错误提示文本
        log.info('获取用户名错误提示文本')
        if data['casetype'] =='用户名错误' \
                or data['casetype'] =='用户名错误1' \
                or data['casetype'] =='用户名错误2' \
                or data['casetype'] =='用户名错误3':
            self.nametext =driver.get_text(self.ADDUSER_NAMETEXT)
        log.info('获取姓名错误提示文本')
        if data['casetype'] =='姓名错误':
            self.realnametext =driver.get_text(self.ADDUSER_RLNMTEXT)
        log.info('获取角色错误提示文本')
        if data['casetype'] =='角色错误':
            self.roletext =driver.get_text(self.ADDUSER_ROLETEXT)
        log.info('获取密码错误提示文本')
        if data['casetype'] =='密码错误':
            self.pwd1text =driver.get_text(self.ADDUSER_PWD1TEXT)
        log.info('获取邮箱错误提示文本')
        if data['casetype'] =='邮箱错误' \
                or data['casetype'] =='邮箱错误1'\
                or data['casetype'] =='邮箱错误2' \
                or data['casetype'] == '邮箱错误3':
            self.emailtext =driver.get_text(self.ADDUSER_EMAILTEXT)
        driver.switch_default_frame()