from base.base_page import RanzhiBasePage
from base.log import Log


class RanzhiDocsPage(RanzhiBasePage):
    DOCS_WEND = "x,.//*[@id='s-menu-4']/button"
    DOCS_FRAME = "iframe-4"
    DOCS_JIAN = 'createButton'
    DOCS_KULX = 'libType'
    DOCS_MZI = 'name'
    DOCS_SHOUQ = "x,.//*[@id='users_chosen']/ul"
    DOCS_GROUP1 = "x,.//*[@id='groupTR']/td/label[1]"
    DOCS_GROUP2 = "x,.//*[@id='groupTR']/td/label[2]"
    DOCS_GROUP3 = "x,.//*[@id='groupTR']/td/label[3]"
    DOCS_GROUP4 = "x,.//*[@id='groupTR']/td/label[4]"
    DOCS_GROUP5 = "x,.//*[@id='groupTR']/td/label[5]"
    DOCS_BUTTON = 'submit'
    DOCS_XMSS = "x,.//*[@id='project_chosen']/a/div"
    DOCS_INPUT = "s,.chosen-search>input"
    DOCS_FENLEI = "x,.//*[@id='treebox']/div[2]/div/a"
    DOCS_LEI1 = "n,children[1]"
    DOCS_LEI2 = "n,children[2]"
    DOCS_LEI3 = "n,children[3]"
    DOCS_LEI4 = "n,children[4]"
    DOCS_LEI5 = "n,children[5]"
    ADOC_SHOUYE = "x,.//*[@id='mainNavbar']/ul/li[1]/a"
    ADDOC_XMUKU = "x,.//*[@id='libs']/div[1]/div/div[2]/a[1]"
    ADDOC_CJWD = "x,.//*[@id='menuActions']/a"
    ADDOC_SHUXING = "x,.//*[@id='module']"
    ADDOC_WDLEI = "x,.//*[@id='ajaxForm']/table/tbody/tr[4]/td"
    ADDOC_WEND = "x,.//*[@id='ajaxForm']/table/tbody/tr[4]/td/label[1]"
    ADDOC_LIEJIE = "x,.//*[@id='ajaxForm']/table/tbody/tr[4]/td/label[2]"
    ADDOC_WENG = "x,.//*[@id='ajaxForm']/table/tbody/tr[4]/td/label[1]"
    ADDOC_LIANJIE = "x,.//*[@id='ajaxForm']/table/tbody/tr[4]/td/label[2]"
    ADDOC_TITLE = "title"
    ADDOC_DUANL = "x,.//*[@id='edui3_button_body']"
    ADDOC_GS = "x,.//*[@id='edui5']/div/div"
    ADDOC_ZWEN = "x,html/body"
    ADDOC_KEY = "keywords"
    ADDOC_FUJIAN = "x,.//*[@id='fileBox1']/tbody/tr/td[1]/div/input"
    ADDOC_URL = "url"
    ADDOC_ZHAIY = "digest"
    ADDZDY_WEND = "x,.//*[@id='libs']/div[2]/div[1]/div/a"
    def docs(self,data):
        driver = self.base_driver
        # 休眠等待
        driver.sleep(1)
        log = Log('..\\logs')
        # 点击文档
        log.info('点击文档')
        driver.click(self.DOCS_WEND)
        driver.sleep(1)
        # 点击创建文档库
        log.info('点击创建文档库')
        driver.switch_to_frame(self.DOCS_FRAME)
        driver.sleep(1)
        driver.click(self.DOCS_JIAN)
        # 编辑文档库类型
        log.info('编辑文档库类型')
        driver.select_by_visible_text(self.DOCS_KULX, data['libtype'])
        driver.sleep(1)
        if data['libtype'] == '自定义文档库':
            # 编辑文档库名称
            log.info('编辑文档库名称')
            driver.click(self.DOCS_MZI)
            driver.type1(self.DOCS_MZI,data['name'])
            driver.sleep(1)
            # 编辑文档库授权用户
            log.info('编辑文档库授权用户')
            driver.click(self.DOCS_SHOUQ)
            driver.type1(self.DOCS_SHOUQ,data['username'])
            # 编辑文档库授权分组
            log.info('编辑文档库授权分组')
            if data['group'] == '管理员':
                driver.click(self.DOCS_GROUP1)
            if data['group'] == '财务专员':
                driver.click(self.DOCS_GROUP2)
            if data['group'] == '销售经理':
                driver.click(self.DOCS_GROUP3)
            if data['group'] == '销售人员':
                driver.click(self.DOCS_GROUP4)
            if data['group'] == '普通用户':
                driver.click(self.DOCS_GROUP5)
            #点击保存
            log.info('点击保存')
            driver.click(self.DOCS_BUTTON)
            driver.sleep(2)
        if data['libtype'] == '项目文档库':
            #编辑所属项目
            log.info('编辑所属项目')
            driver.click(self.DOCS_XMSS)
            driver.type1(self.DOCS_INPUT,'太阳当空照，花儿对我笑')
            # 编辑文档库名称
            log.info('编辑文档库名称')
            driver.click(self.DOCS_MZI)
            driver.type1(self.DOCS_MZI,data['name'])
            # 编辑文档库授权用户
            log.info('编辑文档库授权用户')
            driver.click(self.DOCS_SHOUQ)
            driver.type1(self.DOCS_SHOUQ,data['username'])
            # 编辑文档库授权分组
            log.info('编辑文档库授权分组')
            if data['group'] == '管理员':
                driver.click(self.DOCS_GROUP1)
            if data['group'] == '财务专员':
                driver.click(self.DOCS_GROUP2)
            if data['group'] == '销售经理':
                driver.click(self.DOCS_GROUP3)
            if data['group'] == '销售人员':
                driver.click(self.DOCS_GROUP4)
            if data['group'] == '普通用户':
                driver.click(self.DOCS_GROUP5)
            #点击保存
            log.info('点击保存')
            driver.click(self.DOCS_BUTTON)
            driver.sleep(2)
        # 添加维护分类
        # driver.click(self.DOCS_FENLEI)
        # driver.sleep(1)
        # 编辑类目
        # driver.type1(self.DOCS_LEI1, '金融')
        # driver.type1(self.DOCS_LEI2, '汽车')
        # driver.type1(self.DOCS_LEI3, '旅游')
        # driver.type1(self.DOCS_LEI4, '美食')
        # driver.type1(self.DOCS_LEI5, '人道')
        # driver.sleep(1)
        # driver.click(self.DOCS_BUTTON)
        # driver.sleep(2)
        log.info('跳出最外层框架')
        driver.switch_default_frame()
        driver.sleep(2)

    def adddoc(self, data):
        driver = self.base_driver
        log = Log('..\\logs')
        # 休眠等待
        driver.sleep(1)
        # 点击文档
        log.info('点击文档')
        driver.click(self.DOCS_WEND)
        driver.sleep(1)
        #点击首页
        log.info('点击首页')
        driver.switch_to_frame(self.DOCS_FRAME)
        driver.click(self.ADOC_SHOUYE)
        #点击我的项目库
        log.info('点击我的项目库')
        driver.click(self.ADDOC_XMUKU)
        #点击创建文档
        driver.click(self.ADDOC_CJWD)
        #编辑所属分类
        log.info('选择所属分类')
        driver.click(self.ADDOC_SHUXING)
        driver.select_by_visible_text(self.ADDOC_SHUXING,data['module'])
        #编辑文档库授权用户
        log.info('选择授权用户')
        driver.click(self.DOCS_SHOUQ)
        driver.type1(self.DOCS_SHOUQ,data['username'])
        # 编辑文档库授权分组
        log.info('选择授权分组')
        if data['group'] == '管理员':
            driver.click(self.DOCS_GROUP1)
        if data['group'] == '财务专员':
            driver.click(self.DOCS_GROUP2)
        if data['group'] == '销售经理':
            driver.click(self.DOCS_GROUP3)
        if data['group'] == '销售人员':
            driver.click(self.DOCS_GROUP4)
        if data['group'] == '普通用户':
            driver.click(self.DOCS_GROUP5)
            log.info('选择文档')
        if data['type'] == '文档':
            driver.click(self.ADDOC_WENG)
            log.info('输入文档标题')
            driver.click(self.ADDOC_TITLE)
            driver.type(self.ADDOC_TITLE, data['title'])
            log.info('点击段落')
            driver.click1(self.ADDOC_DUANL)
            driver.click(self.ADDOC_GS)
            log.info('输入文档正文')
            driver.type2(self.ADDOC_ZWEN, data['body'])
            log.info('输入关键字')
            driver.type(self.ADDOC_KEY, data['key'])
            log.info('输入文档摘要')
            driver.click(self.ADDOC_ZHAIY)
            driver.type1(self.ADDOC_ZHAIY,data['body'])
        if data['type'] == '链接':
            log.info('选择链接')
            driver.click(self.ADDOC_LIANJIE)
            log.info('输入文档标题')
            driver.click(self.ADDOC_LIEJIE)
            driver.type1(self.ADDOC_TITLE, data['title'])
            log.info('输入url')
            driver.type1(self.ADDOC_URL,'http://baidu.com')
            log.info('输入关键字')
            driver.click(self.ADDOC_KEY)
            driver.type1(self.ADDOC_KEY, data['key'])
            log.info('输入文档摘要')
            driver.click(self.ADDOC_ZHAIY)
            driver.type1(self.ADDOC_ZHAIY,data['body'])
        #上传附件
        log.info('上传附件')
        driver.type2(self.ADDOC_FUJIAN,r"C:\Users\hzpower\PycharmProjects\ranzhi39\data\adddoc.csv")
        #点击保存
        log.info('点击保存')
        driver.click(self.DOCS_BUTTON)
        driver.sleep(2)
        driver.switch_default_frame()

