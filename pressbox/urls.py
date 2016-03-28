from django.conf.urls import include, url

from pressbox.views import press_detail, press_list


urlpatterns = patterns('',

url(r'^(?P<slug>[-\w]+)/$',
    view = press_detail,
    name= 'press_detail'),

url(r'^$',
    view = press_list,
    name = 'press_list'),

)

#TODO:
#RSS press items
