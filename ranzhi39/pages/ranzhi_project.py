from base.base_page import RanzhiBasePage
from base.log import Log


class RanzhiProjectPage(RanzhiBasePage):
    PROJ_XMU = "x,.//*[@id='s-menu-3']/button"
    PROJ_FRAME = 'iframe-3'
    PROJ_QUKUAI = "x,.//*[@id='dashboard']/div[2]/a"
    PROJ_QUK = 'blocks'
    PROJ_TITLE = 'title'
    PROJ_KUANGD = 'grid'
    PROJ_YANSE = "x,.//*[@id='ajaxForm']/table/tbody/tr[2]/td/div/div/div/button"
    PROJ_LEIX = "x,.//*[@id='paramstype_chosen']/a"
    PROJ_LEIXING = "x,.//*[@id='paramstype_chosen']/a"
    PROJ_NUM = "x,.//*[@id='params[num]']"
    PROJ_ORDERBY = "x,.//*[@id='paramsorderBy_chosen']/a"
    PROJ_DSTATUS = "x,.//*[@id='paramsstatus_chosen']/ul"
    PROJ_BUTTON = 'submit'
    PROJ_STATUS = "x,.//*[@id='paramsstatus_chosen']/a/div"
    PROJ_JINXZ = "x,.//*[@id='paramsstatus_chosen']/div/div/input"
    def project(self,data):
        driver =self.base_driver
        #休眠等待
        # driver.sleep(1)
        #点击项目
        log = Log('logs')
        log.info('点击项目')
        driver.click(self.PROJ_XMU)
        driver.sleep(1)
        #点击添加区块
        log.info('点击添加区块')
        driver.switch_to_frame(self.PROJ_FRAME)
        driver.click(self.PROJ_QUKUAI)
        driver.sleep(1)
        driver.select_by_visible_text(self.PROJ_QUK, data['blocks'])
        driver.sleep(1)
        #编辑项目类型
        if data['blocks'] == '任务列表':
            # 输入任务区块名称
            log.info('输入任务区块名称')
            driver.click(self.PROJ_TITLE)
            driver.type1(self.PROJ_TITLE,data['title'])
            #编辑外观
            log.info('编辑外观')
            driver.select_by_visible_text(self.PROJ_KUANGD,data['grid'])
            driver.get_attribute(self.PROJ_YANSE,data['data-id'])
            #编辑类型
            log.info('编辑类型')
            driver.click(self.PROJ_LEIXING)
            driver.type1(self.PROJ_LEIX,'由我创建')
            #编辑数量
            log.info('编辑数量')
            driver.click(self.PROJ_NUM)
            driver.type(self.PROJ_NUM,data['num'])
            #编辑排序
            log.info('编辑排序')
            driver.click(self.PROJ_ORDERBY)
            driver.type1(self.PROJ_ORDERBY,'优先级递增')
            #编辑任务状态
            log.info('编辑任务状态')
            driver.click(self.PROJ_DSTATUS)
            driver.type1(self.PROJ_DSTATUS,'已关闭')
            #点击保存
            log.info('点击保存')
            driver.click(self.PROJ_BUTTON)
        if data['blocks'] == '项目列表':
            driver.type1(self.PROJ_TITLE, data['title'])
            # 编辑外观
            log.info('编辑外观')
            driver.select_by_visible_text(self.PROJ_KUANGD, data['grid'])
            driver.get_attribute(self.PROJ_YANSE, data['data-id'])
            # 编辑状态
            log.info('编辑状态')
            driver.click(self.PROJ_STATUS)
            driver.type1(self.PROJ_JINXZ,'我参与的')
            # 编辑数量
            log.info('编辑数量')
            driver.click(self.PROJ_NUM)
            driver.type(self.PROJ_NUM, data['num'])
            # 编辑排序
            log.info('编辑排序')
            driver.click(self.PROJ_ORDERBY)
            driver.type1(self.PROJ_ORDERBY, '优先级递增')
            # 点击保存
            log.info('点击保存')
            driver.click(self.PROJ_BUTTON)
        log.info('跳出最外层框架')
        driver.switch_default_frame()
