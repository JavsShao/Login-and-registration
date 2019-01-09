from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女")
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(auto_now_add=True)

    # 使用__str__帮助人性化显示对象信息
    def __str__(self):
        return self.name

    # 元数据定义用户按创建时间的反序列排列，也就是最近的最先显示
    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"