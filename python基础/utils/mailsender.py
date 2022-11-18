# -*- coding: utf-8 -*-
"""
====================================
@File Name ：mailsender.py
@Time ： 2022/11/17 16:57
@Program IDE ：PyCharm
@Create by Author ： stone
@Describe：发送邮件工具类
====================================
"""
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class mailsender(object):
    def __init__(self, host, port):
        self.smtp = smtplib.SMTP
        self.smtp_ssl = smtplib.SMTP_SSL()
        self.smtp.connect(host, port)
        self.user = None
        self.pwd = None

    def login(self, user, pwd):
        """
         实现用户登录
        :param user: 邮箱用户名
        :param pwd: 登录密码
        :return:
        """
        self.user = user
        self.smtp.login(user, pwd)

    def add_attachment(self, filename):
        """
        添加附件
        :param filename: 附件的路径
        :return:
        """
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(open(filename, 'rb').read())
        att.add_header("Content-Disposition", 'attachment', filename=('utf-8', '', filename))
        encoders.encode_base64(att)
        return att

    def add_img(self, filename, image_id):
        """
        添加正文中图片
        :param filename: 图片路径
        :param image_id: 图片中ID机的标识符
        :return:
        """
        msg_image = MIMEBase(open(filename, 'rb').read())
        # 将指定的Content-ID,<img>,在html的src中找到
        msg_image.add_header("Content_ID", image_id)
        return msg_image

    def structure_email(self, email_info):
        """
        构建邮件
        :param email_info:
        :return:
        """
        msg = MIMEMultipart('alternaive')
        if email_info.get("is_html"):
            # html 格式
            contents = MIMEText(email_info.get("content"), "html", _charset='utf-8')
        else:
            contents = MIMEText(email_info.get("content"), "palin", _charset="utf-8")
        msg.attach(contents)
        msg['subject'] = email_info.get("subject")
        msg['from'] = self.user
        msg['to'] = email_info.get('send_target')
        image_attachments = email_info.get("attachments", {})
        for image_id, image_filename in image_attachments.items():
            msg.attach(self.add_img(image_filename, image_id))
        return msg

    def send(self, msg, to_addr):
        """
        发送邮件
        :param msg: 邮件体
        :param to_addr: 收件人
        :return:
        """
        self.smtp.sendmail(self.user, to_addr, msg.as_string())
        self.smtp.quit()


if __name__ == '__main__':
    email_host = "smtp.163.com"
    email_port = "25"
    user = "92066@163.com"
    password = "password"
    message_data = {
        "creator": "00000",  # 创建人
        "create_time": 1345678123456,  # 创建时间
        "subject": "邮件主题",
        "content": '<font color=red> 官网业务周平均延时图表 :<br><img src="cid:image_id_1"><br>详细内容见附件</font>',
        # image_id_1这个是和添加图片用的id对应上
        "send_target": ["123@qq.com"],
        "notice_type": 1,  # 1-邮件，2-短信，3-web
        "status": 1,  # 1-待发送，2-发送成功，3发送失败
        "try_times": 0,  # 尝试次数
        "is_deleted": 0,  # 0-正常，1-已删除
        "attachments": [],  # 附件列表
        "is_html": 0,  # 0-正常文本，1-HTML
        "image_attachments": {"image_id_1": ""}  # 正文是否为HTML,且带图片
    }
    email = mailsender(email_host, email_port)
    email.login(user, password)
    msg = email.structure_email(message_data)
    email.send(msg, message_data.get("send_target"))
