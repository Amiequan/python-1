import smtplib
import time
import unittest
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from base.html_test_runner import HtmlTestRunner

class UCKeFuTestRunner(object):

    def runner(self):
        '''创建测试套件和生成测试报告'''
        # 实例化TestSuite类
        test_suite = unittest.TestSuite()
        # 添加测试用例到测试套件test_suite
        case_path = 'cases'
        discover = unittest.defaultTestLoader.discover(case_path,
                                            pattern='uckefu_test*.py',
                                            top_level_dir=None)
        print('discover:',discover)
        for testsuite in discover:
            print('testsuite:',testsuite)
            for test_case in testsuite:
                print('test_case:',test_case)
                test_suite.addTests(test_case)
        print('test_suite:',test_suite)
        # 创建测试报告文件（没有会自动生成）
        report_path = 'reports\\uckefu_test_report_%s.html' \
                      %time.strftime("%Y%m%d-%H%M%S",time.localtime())
        report_file = open(report_path,'wb')
        test_runner = HtmlTestRunner(report_file,
                                     title='UCKeFu自动化测试报告',
                                     description='测试详情')
        # 运行测试用例
        test_runner.run(test_suite)
        report_file.close()

        # 发邮件相关参数
        smtpserver = 'smtp.qq.com'
        sender = '1713081402@qq.com'
        a = 'cezvnhicwdnhefjh'  #qq授权码
        psw = a
        port = 465
        receiver = ['1435787467@qq.com']
        # receiver = ['linaichao@cdtest.cn','1435787467@qq.com']
        # 实例化发送附件的对象
        msg = MIMEMultipart()
        msg['from'] = sender
        msg['to'] = ';'.join(receiver)
        msg['subject'] = '这个是uckefu项目自动化测试报告主题'
        with open(report_path,'rb') as rp:
            uckefu_mail_body = rp.read()
        '''正文'''
        body = MIMEText(uckefu_mail_body,'html','utf8')
        msg.attach(body)
        '''附件'''
        att = MIMEText(uckefu_mail_body,'base64','utf8')
        att['Content-Type'] = 'application/octet-stream'
        att['Content-Disposition'] = 'attachment;filename ="%s"' %report_path
        msg.attach(att)
        '''发送邮件'''
        smpt = smtplib.SMTP_SSL(smtpserver,port)
        smpt.login(sender,psw)
        smpt.sendmail(sender,receiver,msg.as_string())
        smpt.close()



