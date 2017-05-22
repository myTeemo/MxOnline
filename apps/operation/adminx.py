# -*- coding: utf-8 -*-
import xadmin

from .models import UserAsk
from .models import CouserComments
from .models import UserFavorite
from .models import UserMessage
from .models import UserCourse


__author__ = "Eilene HE"
__date__ = '17/5/22 21:45'


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name']
    list_filter = ['name','mobile','course_name','add_time']


class CourseCommentAdmin(object):
    list_display = ['user','course','comments','add_time']
    search_fields = ['user','course','comments']
    list_filter = ['user','course','comments','add_time']


class UserFavoriteAdmin(object):
    list_display = ['user','fav_id','fav_type','add_time']
    search_fields = ['user','fav_id','fav_type']
    list_filter = ['user','fav_id','fav_type','add_time']


class UserMessageAdmin(object):
    list_display = ['user','message','has_read','add_time']
    search_fields = ['user','message','has_read']
    list_filter = ['user','message','has_read']


class UserCourseAdmin(object):
    list_display = ['user','course','add_time']
    search_fields = ['user','course']
    list_filter = ['user','course','add_time']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CouserComments,CourseCommentAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)


