# -*- coding: utf-8 -*-
from random import Random

from django.core.mail import send_mail
from MxOnline.settings import EMAIL_FROM

from users.models import EmailVerifyRecord
__author__ = "Eilene HE"
__date__ = '17/5/25 23:27'


def random_str(random_length = 8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456890'
    length = len(chars)-1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email, send_type = 'register'):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''
    if send_type == 'register':
        email_title = '幕学在线网注册激活链接'
        email_body = '请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    if send_type == 'forget':
        email_title = ' 幕学网在线密码重置连接'
        email_body = '请点击下面的链接激活你的账号: http://127.0.0.1:8000/reset/{0}'.format(code)

        send_status = send_mail(email_title,email_body,EMAIL_FROM,[email])
        if send_status:
            pass