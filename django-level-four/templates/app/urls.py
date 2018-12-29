from django.conf.urls import url,include
from app import views

# Template Tagging
app_name =  'app'
urlpatterns = [
    url(r'^relative/$',views.relative,name = 'relative'),
    url(r'^other/$',views.other,name='other')
]