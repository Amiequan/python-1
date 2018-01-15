from base.log import Log
from pages.uckefu_login_page import UCKeFuLoginPage

class UCKeFUDialoguesetPage(UCKeFuLoginPage):
    seting_mk = "x,html/body/div[1]/div[2]/div/ul/li[1]/dl/dd[5]/a/i"
    seting_frame = 'maincontent'
    seting_duihua = "x,html/body/div[1]/div/div[1]/div/ul/li[1]/dl/dd[1]/a"
    seting_welcome = "x,.//*[@id='sessionmsg']"
    seting_hint = "x,.//*[@id='noagentmsg']"
    seting_busy = "x,.//*[@id='agentbusymsg']"
    seting_success = "x,.//*[@id='successmsg']"
    seting_finess = "x,.//*[@id='finessmsg']"
    seting_policy = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                    "div/div[2]/div/div/div[6]/div[2]/div/div[2]/div/div/input"
    seting_policy1 = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                     "div/div[2]/div/div/div[6]/div[2]/div/div[2]/div/dl/dd"
    seting_policy2 = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                     "div/div[2]/div/div/div[6]/div[2]/div/div[2]/div/dl/dd[2]"
    seting_maxnum = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div" \
                        "/div/div[2]/div/div/div[7]/div[2]/div/div[2]/div/div/input"
    seting_maxnum1 = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                     "div/div[2]/div/div/div[7]/div[2]/div/div[2]/div/dl/dd"
    seting_ready = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                   "div/div[2]/div/div/div[8]/div[2]/div/div[2]/div/div/input"
    seting_ready1 = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                    "div/div[2]/div/div/div[8]/div[2]/div/div[2]/div/dl/dd"
    seting_historyqy = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                       "div/div[2]/div/div/div[9]/div[2]/div/div[2]/div/span"
    seting_timeoutqy = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                       "div/div[2]/div/div/div[10]/div[2]/div/div[2]/div/span"
    seting_timeout = 'timeout'
    seting_timeoutmsg = 'timeoutmsg'
    seting_timeoutqy1 = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                        "div/div[2]/div/div/div[11]/div[2]/div/div[2]/div/span"
    seting_retimeout = 'retimeout'
    seting_retimeoutmsg = 'retimeoutmsg'
    seting_agenttimeoutqy = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
              "div/div[2]/div/div/div[12]/div[2]/div/div[2]/div/span"
    seting_agenttimeout = 'agenttimeout'
    seting_agenttimeoutmsg = 'agenttimeoutmsg'
    seting_hourcheckqy = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
                         "div/div[2]/div/div/div[13]/div[2]/div/div[2]/div/span"
    seting_hourclick1 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[1]/div/div/div/input"
    seting_hourcheck1 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[1]/div/div/dl/dd"
    seting_hourclick2 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[3]/div/div/div/input"
    seting_hourcheck2 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[3]/div/div/dl/dd"
    seting_hourclick3 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[5]/div/div/div/input"
    seting_hourcheck3 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[5]/div/div/dl/dd"
    seting_hourclick4 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[7]/div/div/div/input"
    seting_hourcheck4 = "x,.//*[@id='hourcheck_tip']/div[3]/div/div[7]/div/div/dl/dd"
    seting_hourchecktip = 'hourcheck_tip'
    seting_degree = "x,html/body/div[1]/div/div[2]/div/form/div[1]/div/div/" \
              "div/div[2]/div/div/div[14]/div[2]/div/div[2]/div/span"
    seting_button = "x,html/body/div[1]/div/div[2]/div/form/div[2]/div[2]/div/div/button[1]"
    seting_reset = "x,html/body/div[1]/div/div[2]/div/form/div[2]/div[2]/div/div/button[2]"
    black_click = "x,html/body/div[1]/div/div[1]/div/ul/li[1]/dl/dd[2]/a"
    black_del = "x,html/body/div[1]/div/div[2]/div/div/div/div[1]/div/table/tbody/tr[2]/td[7]/a"
    black_sure = "x,.//*[@id='layui-layer15']/div[3]/a[1]"
    def dialogueset(self,data):
        driver = self.base_driver
        log = Log('logs')
        # 点击客服设置
        driver.move_to(self.seting_mk)
        driver.click(self.seting_mk)
        driver.sleep(3)
        # 进入iframe
        driver.switch_to_frame(self.seting_frame)
        # 点击对话设置
        driver.click(self.seting_duihua)
        driver.sleep(3)
        # 点击重置
        driver.click(self.seting_reset)
        # 编辑人工坐席接入欢迎语
        driver.type(self.seting_welcome,data['welcomemsg'])
        # 编辑无坐席在线提示信息
        driver.type(self.seting_hint,data['noagentmsg'])
        # 编辑坐席忙时提示消息
        driver.type(self.seting_busy,data['busymsg'])
        # 编辑人工坐席分配成功提示消息
        driver.type(self.seting_success,data['successmsg'])
        # 编辑坐席服务结束提示消息
        driver.type(self.seting_finess,data['finessmsg'])
        # 编辑坐席分配策略
        driver.click(self.seting_policy)
        driver.cycle(self.seting_policy1,data['policy'])
        driver.sleep(1)
        # 编辑坐席分配最大访客数量
        driver.click(self.seting_maxnum)
        driver.cycle(self.seting_maxnum1,data['maxnum'])
        driver.sleep(1)
        # 编辑坐席就绪时分配最大访客数量
        driver.click(self.seting_ready)
        driver.cycle(self.seting_ready1,data['readynum'])
        driver.sleep(1)
        q=driver.is_attribute_in(self.seting_historyqy,'layui-form-checked')
        print('返回值:历史服务坐席优先分配',q)
        if True:
            pass
        if False:
            # 启用历史服务坐席优先分配
            driver.click(self.seting_historyqy)
        # 判断客户超时提醒是否启用
        s=driver.is_element_exist(self.seting_timeout)
        print('返回值:客户超时提醒',s)
        if False:
            # 启用客户超时提醒,编辑超时时长,超时提示信息
            driver.click(self.seting_timeoutqy)
            driver.type(self.seting_timeout,data['timeout'])
            driver.type(self.seting_timeoutmsg,data['timeoutmsg'])
        if True:
            # 禁用客户超时提醒
            driver.click(self.seting_timeoutqy)
        # 判断客户超时提醒后再次超时是否启用
        g=driver.is_element_exist(self.seting_retimeout)
        print('返回值:客户超时提醒后再次超时',g)
        if False:
            # 启用客户超时提醒后再次超时,编辑提醒后再次超时时长,提醒后再次超时后断开的提示消息
            driver.click(self.seting_timeoutqy1)
            driver.type(self.seting_retimeout,data['retimeout'])
            driver.type(self.seting_retimeoutmsg,data['retimeoutmsg'])
        if True:
            # 禁用客户超时提醒后再次超时
            driver.click(self.seting_timeoutqy1)
        # 判断坐席回复超时是否启用
        u=driver.is_element_exist(self.seting_agenttimeout)
        print('返回值:坐席回复超时',u)
        if False:
            # 启用坐席回复超时,编辑超时时长,超时提示信息
            driver.click(self.seting_agenttimeoutqy)
            driver.type(self.seting_agenttimeout,data['agenttimeout'])
            driver.type(self.seting_agenttimeoutmsg,data['agenttimeoutmsg'])
        if True:
            # 禁用坐席回复超时
            driver.click(self.seting_agenttimeoutqy)
        # 判断工作时间段是否启用
        o=driver.is_element_exist(self.seting_hourcheckqy)
        print('返回值:工作时间段',o)
        if False:
            # 启用工作时间段,编辑工作时间段提示信息
            driver.click(self.seting_hourcheckqy)
            # 设置工作开始时间
            driver.click(self.seting_hourclick1)
            driver.cycle(self.seting_hourcheck1,data['hour'])
            driver.click(self.seting_hourclick2)
            driver.cycle(self.seting_hourcheck2,data['minute'])
            driver.click(self.seting_hourclick3)
            # 设置工作结束时间
            driver.cycle(self.seting_hourcheck3,data['rehour'])
            driver.click(self.seting_hourclick4)
            driver.cycle(self.seting_hourcheck4,data['reminute'])
            driver.type2(self.seting_hourchecktip,data['hourchecktip'])
        if True:
            # 禁用工作时间段设置
            driver.click(self.seting_hourcheckqy)
        w=driver.is_attribute_in(self.seting_degree,'layui-form-checked')
        print('返回值:满意度调查',w)
        if True:
            pass
        if False:
            # 启用满意度调查
            driver.click(self.seting_degree)
        # 点击保存
        driver.click(self.seting_button)
        driver.sleep(3)

        # 点击黑名单
        driver.click(self.black_click)
        # 判断一个元素是否存在
        k=driver.is_element_exist(self.black_del)
        print('返回值:删除某一条黑名单',k)
        if False:
            # 删除某一条黑名单
            driver.click(self.black_del)
            # 点击确定
            driver.click(self.black_sure)
        else:
            pass
        driver.switch_to_parent_frame()