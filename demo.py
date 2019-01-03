# coding: utf-8
import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
import os,time
import mimetypes
import unittest
from HTMLTestReportCN import HTMLTestRunner

# 邮箱登录信息，包括发件人、收件人、抄送人、密送
username = '382915567@qq.com'
password = 'kxehdkuotsttbhag'
sender = '382915567@qq.com'  # 发件人邮箱
receiver = 'medo2008@163.com,1102226174@qq.com'  # 多人逗号分开
cc = 'mowencong@sina.com'  # 抄送邮箱, 多人逗号分开
bcc = 'imowencong@gmail.com'  # 秘密抄送邮箱, 多人逗号分开
# 邮件内容和主题
now = time.strftime('%Y-%m-%d %H:%M:%S')
subject = '自动化测试报告' + now
mail_content = '<html><h1>自动化测试报告详情参考附件</h1></html>'


# 所有收信人以及抄送和暗抄对象都一样,
# 放在都一样 server.sendmail(sender, toaddrs, msg.as_string()) 第二个参数toaddrs里面
# 具体区别收信人以及抄送和暗抄对象,
# 都由server.sendmail(sender, toaddrs, msg.as_string()) 第三个参数里面msg里面的关键词决定

msg = MIMEMultipart()
msg.add_header('From', username)
msg.add_header('To', receiver)
msg.add_header('Cc', cc)
msg.add_header('BCc', bcc)
msg.add_header('Subject', subject)
msg.add_header('Date', subject)
msg.attach(MIMEText(mail_content, 'html'))
# 所有收信人信息
toaddrs = [receiver] + [cc] + [bcc]


# 添加附件
def add_attachment(filepath):
    ctype, encoding = mimetypes.guess_type(filepath)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    maintype, subtype = ctype.split("/", 1)
    fp = open(filepath, 'rb')
    attachment = MIMEBase(maintype, subtype)
    attachment.set_payload(fp.read())
    fp.close()
    encoders.encode_base64(attachment)
    baseName = os.path.basename(filepath)
    attachment.add_header('Content-Disposition', 'attachment', filepath=filepath,  filename=baseName)
    msg.attach(attachment)
    print(filepath, 'added')


def new_file(test_dir):
    Files = []
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir + '\\' + fn))
    # 获取最新文件的绝对路径
    filepath = os.path.join(test_dir, lists[-1])
    #    L=file_path.split('\\')
    #    file_path='\\\\'.join(L)
    Files.append(filepath)
    # ctype, encoding = mimetypes.guess_type(filepath)
    baseName = os.path.basename(filepath)
    att = MIMEApplication(open(filepath, 'rb').read())
    att.add_header('Content-Disposition', 'attachment', filename=baseName)
    msg.attach(att)
    print(filepath, 'added')


def send(new_report):
    mail_server = 'smtp.qq.com'
    mail_server_port = 587
    server = smtplib.SMTP(mail_server, mail_server_port)
    # server.set_debuglevel(1) # 调试模式
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(sender, toaddrs, msg.as_string())
    server.quit()


if __name__ == '__main__':
    print('=====AutoTest Start======')

    # Windows的cmd执行：不用绝对路径会报：ImportError:
    test_dir = 'D:\\WKSP\\WILY\\CASES'
    test_report_dir = 'D:\\WKSP\\WILY\\REPORTS'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    now = time.strftime('%Y-%m-%d_%H_%M_%S_')
    filename = test_report_dir + '\\' + now + 'Test_Report.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行详细情况：')
    runner.run(discover)
    fp.close()
    # 取最新测试报告
    new_report = new_file(test_report_dir)
    # 发送邮件，发送最新测试报告html
    send(new_report)
    print('=====AutoTest Finished======')
