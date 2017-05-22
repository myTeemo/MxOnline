# -*- coding: utf-8 -*-
import xadmin

from .models import CityDict
from .models import CourseOrg
from .models import Teacher


__author__ = "Eilene HE"
__date__ = '17/5/22 13:52'


class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name']
    list_filter = ['name','add_time']


class CourseOrgAdmin(object):
    list_display = ['name','desc','click_nums','fav_nums','image','address','city']
    search_fields = ['name','click_nums','fav_nums','address']
    list_filter = ['name','city__name']


class TeacherAdmin(object):
    list_display = ['org','name','work_years','work_company','work_position','points','fav_nums','click_nums','add_time']
    search_fields = ['org','name','work_years','work_company','work_position','points','fav_nums','click_nums']
    list_filter = ['org__name','name','work_years','work_company','work_position','points','fav_nums','click_nums','add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)
xadmin.site.register(Teacher,TeacherAdmin)