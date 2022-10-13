from django.urls import path, re_path, include

from basic_app import views

# This is for TEMPLATE TAGGING
# Django will automatically look for this.
# This is what is matched in relative_url_templates.html file in {% url ... %}
app_name = 'basic_app'

urlpatterns=[
    re_path(r'^relative/$', views.relative, name='relative'),
    re_path(r'^other/$', views.other, name='other'),
]