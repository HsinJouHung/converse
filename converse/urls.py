"""converse URL Configuration

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
from django.urls import path

from home.views import choose_identification
from home.views import supplier_login
from home.views import company_login
from home.views import sales_login
from home.views import delivery_login
from manageperson.views import manage,report,cusanalysis,cuscluster
from salesperson.views import sales,newmember,newsales,checkinventory,new_member,new_order
from supplyperson.views import supply
from deliveryperson.views import delivery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',choose_identification),
    path('home/supplier_login/',supplier_login),
    path('home/sales_login/',sales_login),
    path('home/delivery_login/',delivery_login),
    path('home/company_login/',company_login),
    path('manage/',manage),
    path('sales/',sales),
    path('supply/',supply),
    path('delivery/',delivery),
    path('manage/report/',report),
    path('manage/customer_analysis/',cusanalysis),
    path('manage/customer_cluster/',cuscluster),
    path('sales/new_member/',newmember),
    path('sales/new_sales/',newsales),
    path('sales/check_inventory/',checkinventory),
    path('sales/new_member/member/',new_member),
    path('sales/new_sales/order/',new_order)
]
