"""studentsdb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG
from django.conf.urls import patterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # students url
    url(r'^$', 'studentsdb.students.views.students_list', name='home'),
    # groups url
    url(r'^groups/$', 'studentsdb.students.views.groups_list', name='groups'),
    # add a student
    url(r'^students/add/$', 'studentsdb.students.views.students_add', name='student_add'),
    # edit student
    url(r'^students/(?P<sid>\d+)/edit/$', 'studentsdb.students.views.students_edit', name='student_edit'),
    # delete student
    url(r'^students/(?P<sid>\d+)/delete/$', 'studentsdb.students.views.students_delete', name='student_delete'),
    # add group
    url(r'^groups/add/$', 'studentsdb.students.views.groups_add', name='add_group'),
    # edit group
    url(r'^groups/(?P<gid>\d+)/edit/$', 'studentsdb.students.views.groups_edit', name='edit_group'),
    # delete group
    url(r'^groups/(?P<gid>\d+)/delete/$', 'studentsdb.students.views.groups_delete', name='delete_group'),
    # Test URL
    url(r'^test/$', 'studentsdb.students.views.test', name='test'),
    # Attendance URL
    url(r'^attendance/$', 'studentsdb.students.views.attendance', name='attendance'),
    url(r'^translate/blog/$', 'translator.views.blog', name='start'),

]
if DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$',
                                'django.views.static.serve',
                                {'document_root': MEDIA_ROOT}))