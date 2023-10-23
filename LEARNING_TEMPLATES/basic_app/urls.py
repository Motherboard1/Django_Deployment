from django.urls import re_path
from basic_app import views



app_name = 'basic_app'


urlpatterns = [
      re_path('relative/',views.relative,name='relative'),
      re_path('other/',views.other, name= 'other')
]
