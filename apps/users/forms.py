# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import CaptchaField

__author__ = "Eilene HE"
__date__ = '17/5/24 22:45'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=6)
    captcha = CaptchaField(error_messages={"invalid":u'验证码错误'})

