import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

current_path = os.path.dirname(__file__)
smtp_file_path = os.path.join(current_path, 'reports/禅道自动化测试报告V1.1/禅道自动化测试报告.zip')
#D:/PO_UI_Test_Framework\..\reports/禅道自动化测试报告V1.1/
smtp_server = 'smtp.163.com'  #邮件服务器地址
smtp_sender = '15575953724@163.com' #邮箱名
smtp_senderpassword = 'ZJHYNLTAMEFWYCUE' #邮箱授权码
smtp_receiver = '15575953724@163.com,519834579@qq.com' #收件人
smtp_cc = '505697990@qq.com' #抄送人
smtp_subject='自动化测试报告(测试版)' #邮件主题
smtp_body='来自python邮件自动发送测试' #邮件内容
smtp_file=smtp_file_path

msg = MIMEMultipart()
with open(smtp_file,'rb') as f:
    mime = MIMEBase('zip','zip',filename=smtp_file.split('/')[-1])
    mime.add_header('Content-Disposition','attachment',filename=('gb2312','',smtp_file.split('/')[-1]))
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-Id','0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)
msg.attach(MIMEText(smtp_body,"html","utf-8"))
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject
smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender,password=smtp_senderpassword)
smtp.sendmail(smtp_sender,smtp_receiver.split(',')+smtp_cc.split(','),msg.as_string())

# if smtp_file !=None:
# msg = MIMEMultipart
# with open(smtp_file,'rb') as f:
# mime = MIMEBase('zip','zip',filename=smtp_file.split('/')[-1])
# mime.add_header('Content-Disposition','attachment',filename=('gb2312','',smtp_file.split('/')[-1]))
# mime.add_header('Content-ID','<0>')
# mime.add_header('X-Attachment-Id','0')
# mime.set_payload(f.read())
# encoders.encode_base64(mime)smtp_senderpassword = 'ZJHYNLTAMEFWYCUE'
# smtp_receiver = '505697990@qq.com,15575953724@163.com,519834579@qq.com'
# smtp_cc = ''
# smtp_subject=smtp_subject
# smtp_body=smtp_body
# smtp_file=smtp_file_path
# smtp_file !=None:
# msg = MIMEMultipart
# with open(smtp_file,'rb') as f:
# mime = MIMEBase('zip','zip',filename=smtp_file.split('/')[-1])
# mime.add_header('Content-Disposition','attachment',filename=('gb2312','',smtp_file.split('/')[-1]))
# mime.add_header('Content-ID','<0>')
# mime.add_header('X-Attachment-Id','0')
# mime.set_payload(f.read())
# encoders.encode_base64(mime)