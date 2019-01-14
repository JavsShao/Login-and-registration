import os
from django.core.mail import send_mail, EmailMultiAlternatives

os.environ['DJANGO_SETTINGS_MODULE'] = 'login.settings'

if __name__ == '__main__':

    subject, from_email, to = '来自www.Hamdi.com的测试邮件', 'javs_shao@163.com', 'shaoleei@126.com'
    text_content = "欢迎访问www.baidu.com, 这里是百度的首页!"
    html_content = '<p>欢迎访问<a href="http://www.baidu.com" target=blank>www.liujiangblog.com</a>，这里是百度的首页，全球最大的中文搜索引擎!</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()