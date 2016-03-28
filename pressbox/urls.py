from django.conf.urls import include, url
from pressbox.views import press_detail, press_list


urlpatterns = [url(r'^(?P<slug>[-\w]+)/$',press_detail,name= 'press_detail'),
url(r'^$',press_list, name = 'press_list'),
]
