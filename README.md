# MxOnline在线学习系统

### 系统环境：  

1. django1.9([django1.9](https://www.djangoproject.com/download/))
2. python2.7([python2.7](https://www.python.org/downloads/release/python-2713/))
3. xadmin([github上xadmin最新版](https://github.com/sshwsfc/xadmin))
4. virtualenv/virtualenvwrapper
5. Pillow4.0.0( ```pip install pillow```)
6. django-crispy-forms1.6.1
7. MySQL-python1.2.5

### 2017/05/22 更新内容
1. 使用xadmin第三方后台管理系统取代admin  
2. 注册每一个应用的models
3. 配置xadmin的全局设置,包括设置title,footer,themes,菜单应用折叠  
4. 配置应用在xadmin的菜单显示名称  


- xadmin启动主题功能

在users应用下的adminx.py下定义

```python  

    import xadmin
    from xadmin import views
    
    class BaseSetting(object):
        enable_themes = True
        use_bootswatch = True
        
        
    xadmin.site.register(views.BaseAdminView,BaseSetting)
```


- xadmin中修改标题,页脚和折叠左侧菜单

```python  
    # -*- coding:utf-8 -*-
    import xadmin
    from xadmin import views
    
    
    class GlobalSetting(object):
        site_title = u'标题名称'
        site_footer = u'页脚名称'
        menu_style = 'accordion'


    xadmin.site.register(views.CommAdminView,GlobalSetting)
```

- 配置应用在xadmin左侧名称

以courses应用为例

> 修改courses/apps.py文件
```python  
   # -*-coding:utf-8 -*-
   
   from django.apps import AppConfig
   
   
   class UsersConfig(AppConfig):
        name = 'users'
        verbose_name = u'用户管理' # 新增本行 
```


### 2017/05/23 更新内容

1. 配置静态文件
2. 配置url
3. 配置登录逻辑
4. 配置使用邮箱登录

- 配置静态文件

>项目中会使用静态文件,包括js、css、images等一系列资源文件,使用django配置静态资源文件夹

>在项目的根目录下建立static文件夹,将资源文件放置其中  
>在settings.py中配置字段

```python

   import os
   
   STATICFILES_DIRS = (
       os.path.join(BASE_DIR,'static'),
   )
```

- 配置url

>urls.py配置

```python

    from django.conf.urls import url
    from django.views.generic import TemplateView
    
    urlpattern = [
        url(r'^$',TemplateView.as_view(template_name='index.html'),name='index'),
    ]
    
```

- 登录逻辑配置

> 在users应用下的views.py中编写登录逻辑代码

```python
    # -*- coding:utf-8 -*-
    from django.contrib.auth import authenticate
    from django.contrib.auth import login
    from django.shortcuts import render
    
    def user_login(request):
        if request.method == 'POST':
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')
            
            user = authenticate(username=user_name,password=pass_word)
            
            if user is not None:
                login(request,user)
                return render(request,"index.html",{})
            else:
                return render(request,"login.html",{'msg':'登录名或密码错误'})
        elif request.method == "GET":
            return render(request,"login.html",{})
            
```

> authenticate(username='xxx',password='xxx')
> 上面是固定写法,对传入的用户名和密码进行验证,成功的话返回user对象,这里的user对象就是在usersapp下扩展的UserProfile
> 另外注意authenticate方法中的参数,第一个参数叫username,第二个叫password,一定要加上,否则会报错

> login(request,user)
> 上面是固定写法,第一个参数是request,第二参数是authenticate认证成功后返回的user对象

上面定义成功后在templates中进行判断是否成功登录

```
    {% if request.user.is_authenticated %}
        xxx
    {% else %}
        xxx
    {% endif %}
           

```

- 配置可以使用邮箱登录

> Django默认使用用户名登录,这里修改默认设置,重新配置可以使用邮箱登录

```python
    # 修改users/views.py
    
    from django.contrib.auth.backends import ModelBackend
    from django.db.models import Q
    
    from .models import UserProfile
    
    class CustomBackends(ModelBackend):
        def authenticate(self, username=None, password=None, **kwargs):
            try:
                user = UserProfile.objects.get(Q(username=username)|Q(email=username))
                
                if user.check_password(password):
                    return user
                else:
                    return None
            except Exception as e:
                return None
   
    
    # 配置完毕之后再settings.py中添加字段使之生效
    AUTHENTICATION_BACKENDS = (
        'users.views.CustomBackends',
    )
```

### 2017/05/24更新内容

1. 更改用户登录的方式为基于类的方式
2. 添加Django的表单类,从而进行表单验证
3. 对于表单的验证结果向前台进行输出

- 配置基于类的方式登录

> 通常我们在一些列的教程中看到,views.py中的视图一般是基于函数的方式进行登录
> 但是还可以通过类的方式进行登录,以为类中可以有很多的方法,而如果使用函数的方法进行
> 登录的话需要些很多的方法,看起来不好,显得过于杂乱。

>详细配置如下

```python
    # -*- coding:utf-8 -*-
    # /apps/users/views.py
    from django.shortcuts import render
    from django.contrib.auth import authenticate
    from django.contrib.auth import login
    from django.views.generic.base import View
    
    
    class LoginView(View):
        def get(self,request):
            return render(request,'index.html',{})
        
        def post(self,request):
            user_name = request.POST.get('username','')
            pass_word = request.POST.get('password','')
            
            user = authenticate(username=user_name,password=pass_word)
            
            if user is not None:
                login(request,user)
                return render(request,'index.html',{})
            else:
                return render(request,'login.html',{'msg':'用户名或密码错误'})
        
        
```  

```python
    # MxOnline/urls.py
    from django.conf.urls import url
    from users.views import LoginView
    

    urlpatterns = [
        url(r'^login/$',LoginView.as_view(),name='login')
    ]
    # 这里要配置自己写的类的as_view()方法,一定要加括号
```

- 添加表单进行验证

> Django自带了表单类,我们可以通过继承表单,定义自己的表单,然后在客户端用户提交的数据
> 进行数据库验证之间,进行预先判断。这一步在项目开发过程中,不能缺少

```python
    # /apps/users/forms.py 新建
    
    from django import forms
    
     
    class Login(forms.Form):
        username = forms.CharField(required=True)
        password = forms.CharField(required=True,min_length=5)
    
    
    # 修改 /apps/users/views/LoginView
   
    
    from .forms import LoginForm
    from django.shortcuts import render
    from django.contrib.auth import authenticate
    from django.contrib.auth import login
    
    
    class LoginView(View):
        def get(self,request):
            return render(request,"login.html",{})

        def post(self,request):
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_name = request.POST.get('username','')
                pass_word = request.POST.get('password','')
                user = authenticate(username=user_name,password=pass_word)
                if user is not None:
                    login(request,user)
                    return render(request,'index.html',)
                else:
                    return render(request,'login.html',{'msg':'用户名或密码错误'})
            else:
                return render(request,'login.html',{'login_form':login_form})

```


```html
    <div class="form-group marb20 {% if login_form.errors.username %}errorput{% endif %}">
        <label>用&nbsp;户&nbsp;名</label>
        <input name="username" id="account_l" type="text" placeholder="手机号/邮箱" />
    </div>
    <div class="form-group marb8 {% if login_form.errors.password %}errorput{% endif %}">
        <label>密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码</label>
        <input name="password" id="password_l" type="password" placeholder="请输入您的密码" />
     </div>
    <div class="error btns login-form-tips" id="jsLoginTips">{% for key,error in login_form.errors.items %}{{ error }}{% endfor %}{{ msg }}</div>
```
