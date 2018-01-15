from pages.uckefu_login_page import UCKeFuLoginPage

class UCKeFUSetserviceadPage(UCKeFuLoginPage):
    seting_mk = "x,html/body/div[1]/div[2]/div/ul/li[1]/dl/dd[5]/a/i"
    seting_frame = 'maincontent'
    seting_admg = "x,html/body/div[1]/div/div[1]/div/ul/li[2]/a"
    seting_admgall = "x,html/body/div[1]/div/div[1]/div/ul/li[2]/dl/dd/a"
    seting_entrancead = "s,.layui-btn.layui-btn-small.green"
    seting_adname = "x,.//*[@id='mainajaxwin']/div/form/div[1]/div[1]/div/div/div[1]/div/input"
    seting_adweight = "x,.//*[@id='mainajaxwin']/div/form/div[1]/div[1]" \
                      "/div/div/div[2]/div/div/div/input"
    seting_adweightall = "x,.//*[@id='mainajaxwin']/div/form/div[1]/" \
                       "div[1]/div/div/div[2]/div/div/dl/dd"
    seting_adtypepicture = "x,.//*[@id='mainajaxwin']/div/form/div[1]/" \
                           "div[2]/div/div[1]/div[1]/div/div[1]"
    seting_adtypetext = "x,.//*[@id='mainajaxwin']/div/form/div[1]/" \
                        "div[2]/div/div[1]/div[1]/div/div[2]/i"
    seting_adhinttext = "x,.//*[@id='mainajaxwin']/div/form/div[1]/" \
                        "div[2]/div/div[1]/div[2]/div/input"
    seting_adaddr = "x,.//*[@id='mainajaxwin']/div/form/div[1]/" \
                    "div[2]/div/div[2]/div/div/input"
    seting_adimg = 'imgtarget'
    seting_adfiles = 'files'
    seting_adtext = "x,.//*[@id='text']/div/div/textarea"
    seting_adbutton = "x,.//*[@id='mainajaxwin']/div/form/div[2]/div/button[1]"
    seting_adreset = "x,.//*[@id='mainajaxwin']/div/form/div[2]/div/button[2]"
    def setservicead(self,data):
        driver = self.base_driver
        # 点击客服设置
        driver.move_to(self.seting_mk)
        driver.click(self.seting_mk)
        driver.sleep(3)
        # 进入iframe
        driver.switch_to_frame(self.seting_frame)
        # 获取广告位管理下面的子项
        driver.cycle(self.seting_admgall,data['admg'])
        driver.sleep(3)
        if data['admg'] == '访客入口（技能组窗口）' \
                or data['admg'] == '邀请框（询问窗口）'\
                or data['admg'] == '欢迎提示（对话窗口）'\
                or data['admg'] == '形象展示（对话窗口）':
            # 点击添加广告
            driver.click(self.seting_entrancead)
            driver.switch_to_parent_frame()
            driver.sleep(2)
            # 点击重置
            driver.click(self.seting_adreset)
            # 编辑广告名称
            driver.type1(self.seting_adname,data['name'])
            # 点击权重,获取权重的所有元素
            driver.click(self.seting_adweight)
            driver.cycle(self.seting_adweightall,data['weight'])
            # 编辑广告类型
            if data['adtype'] == '图片':
                driver.switch_to_parent_frame()
                driver.click(self.seting_adtypepicture)
                # 编辑提示文本内容
                driver.type2(self.seting_adhinttext,data['hinttext'])
                driver.sleep(1)
                # 编辑跳转链接地址
                driver.type2(self.seting_adaddr,data['address'])
                # 上传广告图片
                driver.input_file_path(self.seting_adtypetext,data['adtext'])
                # 上传附件
                # driver.input_file_path(self.seting_adfiles,data['files'])
            if data['adtype'] == '文本':
                driver.switch_to_parent_frame()
                driver.click(self.seting_adtypetext)
                # 编辑提示文本内容
                driver.type2(self.seting_adhinttext,data['hinttext'])
                # 编辑跳转链接地址
                driver.type2(self.seting_adaddr,data['address'])
                # 输入广告文本内容
                driver.input(self.seting_adtext,data['adtext'])
                driver.sleep(2)
            # 点击保存
            driver.click(self.seting_adbutton)
            driver.switch_to_parent_frame()