# -*- coding: utf-8 -*-
from django import forms

__author__ = "Eilene HE"
__date__ = '17/5/24 22:45'


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)

