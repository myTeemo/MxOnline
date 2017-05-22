# MxOnline在线学习系统

- 系统环境：  

1. django1.9 
2. python2.7



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
