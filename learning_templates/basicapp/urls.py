from django.conf.urls import url
from basicapp import views

#Template Tagging
app_name='basicapp'
#this name is always fixed

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
