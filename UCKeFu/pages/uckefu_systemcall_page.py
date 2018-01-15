from pages.uckefu_login_page import UCKeFuLoginPage

class UCKeFUSystemcallPage(UCKeFuLoginPage):
    system_mg = "x,html/body/div[1]/div[1]/div/ul/li[3]/a"
    system_iframe = 'admin'
    system_call = "x,html/body/div[1]/div[1]/div/ul/li[4]/a"
    system_voice = "x,html/body/div[1]/div[1]/div/ul/li[4]/dl/dd/a"
    system_serverset = "x,.//*[@id='pbxHostTab']/li[1]/a"
    system_addservice = "x,.//*[@id='callCenterContent']/div/div/h1/span/button"
    system_name = "x,.//*[@id='mainajaxwin']/div/form/div[1]/div[1]/input"
    system_hostname = "x,.//*[@id='mainajaxwin']/div/form/div[2]/div[1]/input"
    system_ipaddr = "x,.//*[@id='mainajaxwin']/div/form/div[3]/div[1]/input"
    system_port = "x,.//*[@id='mainajaxwin']/div/form/div[4]/div[1]/input"
    system_pwd = "x,.//*[@id='mainajaxwin']/div/form/div[5]/div[1]/input"
    system_button = "x,.//*[@id='mainajaxwin']/div/form/div[6]/div/button[1]"
    system_reset = "x,.//*[@id='mainajaxwin']/div/form/div[6]/div/button[2]"
    system_sure = "s,.layui-layer-btn0"
    def systemcall(self,data):
        driver = self.base_driver
        # 点击系统管理员
        driver.move_to(self.system_mg)
        driver.click(self.system_mg)
        driver.sleep(3)
        # 进入iframe
        driver.switch_to_frame(self.system_iframe)
        # 移到到呼叫中心
        driver.move_to(self.system_call)
        # 点击语言平台
        driver.click(self.system_voice)
        driver.sleep(3)
        # 点击服务配置
        driver.click(self.system_serverset)
        driver.sleep(1)
        # 点击添加新服务器
        driver.click(self.system_addservice)
        driver.sleep(1)
        driver.switch_to_parent_frame()
        # 点击重置
        driver.click(self.system_reset)
        # 编辑服务器相关项
        driver.type(self.system_name,data['name'])
        driver.type(self.system_hostname,data['hostname'])
        driver.type(self.system_ipaddr,data['ipaddr'])
        driver.type(self.system_port,data['port'])
        driver.type(self.system_pwd,data['pwd'])
        driver.sleep(1)
        # 点击保存
        driver.click(self.system_button)
        driver.sleep(1)
        # 点击确定
        driver.click(self.system_sure)