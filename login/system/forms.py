from django import forms
from . import models


class UserForm(forms.Form):
    class Meta:
        model = models.User
        fields = ['name', 'password']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, *kwargs)
        self.fields['name'].lable = '用户名'
        self.fields['password'].lable = '密码'
