import os
from django.core.mail import send_mail


os.environ['DJANGO_SETTINGS_MODULE'] = 'login.settings'

if __name__ == '__main__':

    send_mail(
        '这是测试邮件',
        '来自：Hamdi',
        'javs_shao@163.com',
        ['shaoleei@126.com'],
    )