from django.urls import path
from .import views

urlpatterns = [
	path('',views.report, name='report'),
	path('purchase_report',views.purchase_report, name='purchase_report'),
	path('purchase_order_report',views.purchase_order_report, name='purchase_order_report'),
	path('dispatch_order_report',views.dispatch_order_report, name='dispatch_order_report'),
	path('daily_order_report',views.daily_order_report, name='daily_order_report'),

]