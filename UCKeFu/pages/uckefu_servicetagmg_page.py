from pages.uckefu_login_page import UCKeFuLoginPage

class UCKeFUSetservicetagPage(UCKeFuLoginPage):
    seting_mk = "x,html/body/div[1]/div[2]/div/ul/li[1]/dl/dd[5]/a/i"
    seting_frame = 'maincontent'
    seting_tagmg = "x,html/body/div[1]/div/div[1]/div/ul/li[3]/a"
    seting_tag = "x,html/body/div[1]/div/div[1]/div/ul/li[3]/dl/dd/a"
    seting_entrancetag = "x,html/body/div[1]/div/div[2]/div/div/div/h1/span/button"
    seting_tagname = "x,.//*[@id='mainajaxwin']/div/form/div[1]/div/input"
    seting_tagcolors = "x,.//*[@id='mainajaxwin']/div/form/div[2]/div/div/div"
    seting_adbutton = "x,.//button[text()='立即提交']"
    seting_adreset = "x,.//button[text()='重置']"
    seting_editor = "l,编辑标签"
    seting_del = "l,请确认是否删除标签？"
    seting_sure = "x,.//*[@id='layui-layer16']/div/a[1]"
    def setservicetag(self,data):
        driver = self.base_driver
        if data['tagmg'] == '咨询客户' \
                or data['tagmg'] == '工单' \
                or data['tagmg'] == '呼叫中心服务类型' \
                or data['tagmg'] == '知识库知识' \
                or data['tagmg'] == '服务类型':
            # 点击客服设置
            driver.move_to(self.seting_mk)
            driver.click(self.seting_mk)
            driver.sleep(3)
            # 进入iframe
            driver.switch_to_frame(self.seting_frame)
            # 鼠标移到标签管理
            driver.move_to(self.seting_tagmg)
            # 获取标签管理的子项
            driver.cycle(self.seting_tag, data['tagmg'])
            # 点击添加标签
            driver.click(self.seting_entrancetag)
            # 跳出上一层iframe
            driver.switch_to_parent_frame()
            driver.sleep(3)
            # 点击重置
            driver.click(self.seting_adreset)
            driver.sleep(10)
            # 编辑标签
            driver.type1(self.seting_tagname,data['name'])
            # 获取背景颜色的所有元素
            driver.get_attribute(self.seting_tagcolors,data['color'])
            driver.sleep(1)
            # pass    # 居然可以成功提交/之后什么都没有居然也可以保存成功/什么鬼??!!
            # 点击立即提交
            driver.click(self.seting_adbutton)    # 保存成功了居然还报错
            # 进入iframe
            # driver.switch_to_frame(self.seting_frame)
            driver.sleep(1)
            # 点击编辑标签
            # driver.click(self.seting_editor)
            # driver.switch_to_parent_frame()
            # # 点击重置-保存
            # driver.click(self.seting_adreset)
            # driver.click(self.seting_adbutton)
            # # 进入iframe
            # driver.switch_to_frame(self.seting_frame)
            # driver.sleep(1)
            # # 点击删除标签
            # driver.click(self.seting_del)
            # driver.click(self.seting_sure)
            # driver.sleep(3)