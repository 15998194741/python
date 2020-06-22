"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url
from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^favicon.ico/$', views.index2, name='index1'),
    url(r'^about/$', views.about, name='about'),
    url(r'^new/$', views.new, name='new'),
    url(r'^product/$', views.product, name='product'),
    url(r'^case/$', views.case, name='case'),
    url(r'^casesite/$',views.casesite,name='casesite'),
    url(r'^qlogin/$', views.login1, name='loglogin'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^login/$',views.do_login,name='login'),
    url(r'^qlogout/$', views.do_logout, name='logout'),
    url(r'^productsite/$',views.productsite,name='productsite'),
    url(r'^text/',views.text,name='text'),
    url(r'^test1/$', views.test1, name='test1'),
    url(r'^test/$', views.test, name='test'),
    url(r'^chat/$',views.Chat,name='chat'),
    url(r'^tahc/$', views.ta.as_view(), name='tahc'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^delete_new',views.delete_news,name='deletenew'),
    url(r'^delete_case', views.delete_case, name='delete_case'),
    url(r'^case_upload', views.case_upload, name='case_upload'),
url(r'^delete_product', views.delete_product, name='delete_product'),
    url(r'^product_upload', views.product_upload, name='product_upload'),

    # url(r'^chatone/$',views.chatone,name='chatone')

]
