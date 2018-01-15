import smtplib
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from base.html_test_runner import HtmlTestRunner
from cases.ranzhi_test_adduser import RanzhiTestAdduser
from cases.ranzhi_test_login import RanzhiTestLogin

class RanzhiTestRunner(object):
    def runner(self):
        '''创建测试套件和生成测试报告'''
        #实例化TestSuite类
        test_suite = unittest.TestSuite()
        #添加测试用例到测试套件test_suite
        # test_suite.addTest(RanzhiTestLogin('test_login'))
        # test_suite.addTest(RanzhiTestAdduser('test_adduser'))
        case_path = 'cases'
        discover = unittest.defaultTestLoader.discover(case_path,
                                            pattern='ranzhi_test*.py',
                                            top_level_dir=None)
        print('discover:',discover)
        for testsuite in discover:
            print('testsuite:',testsuite)
            for test_case in testsuite:
                print('test_case:',test_case)
                test_suite.addTests(test_case)
        print('test_suite:',test_suite)
        #创建测试报告文件（没有会自动生成
        # report_path = 'ranzhi_test_report_%s.html'%time.time()
        report_path = 'reports\\ranzhi_test_report_%s.html' \
                      % time.strftime('%Y%m%d-%H%M%S',time.localtime())
        report_file = open(report_path,'wb')
        test_runner = HtmlTestRunner(report_file,
                                     title='Ranzhi自动化测试报告',
                                     description='测试详情')
        #运行测试用例
        test_runner.run(test_suite)
        report_file.close()

        #发送邮件相关参数
        smtpsever = 'smtp.qq.com'
        sender = '417307606@qq.com'
        psw = 'lhltusfystwwbgfe'    #16位授权码
        port = 465
        # recevice = '274859299@qq.com' and  '1435787467@qq.com'
        recevice = '274859299@qq.com;1435787467@qq.com'
        # 实例化发送附件对象
        msg = MIMEMultipart()
        msg['from'] = sender
        # msg['to'] = recevice
        msg['to'] = ';'.join(recevice)
        msg['subject'] = '这个是xx项目自动化测试报告主题'
        # with...as...与 open（）区别:with...as...可以自动关闭文件
        with open(report_path,'rb') as rp:
            ranzhi_mail_body = rp.read()
        '''正文'''
        body = MIMEText(ranzhi_mail_body,'html','utf8')
        msg.attach(body)
        '''附件'''
        att = MIMEText(ranzhi_mail_body,'base64','utf8')
        att['Content-Type'] = 'application/octet-stream'
        #report_path是生成报告的名称
        att['Content-Disposition'] = 'attachment;filename = "%s"'%report_path
        msg.attach(att)
        '''发送邮箱'''
        smtp = smtplib.SMTP_SSL(smtpsever,port)
        smtp.login(sender,psw)
        smtp.sendmail(sender,recevice,msg.as_string())
        smtp.close()