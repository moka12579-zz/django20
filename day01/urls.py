from django.urls import path, re_path

from day01.views import view_func, view_re_func, view_func_v1, view_template

urlpatterns = [
    path('view/name/', view_func, name='name'),
    path('view/v1/', view_func_v1, name='v1'),
    path('temp/', view_template, name='template'),
    re_path('^9\d{4}/$', view_re_func),
]