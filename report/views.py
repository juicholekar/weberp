from django.shortcuts import render
from material_transaction.models import Purchase
from production.models import Production

import datetime
from .filters import UserFilter

# Create your views here.
def report(request):
	return render(request,'report/report.html')

def purchase_report(request):
	if request.method == 'GET':
		purchase_id = request.GET.get('search')
		try:
			status = Purchase.objects.filter(id=purchase_id)
		except Purchase.DoesNotExist:
			status = None
		return render(request, 'report/purchase_report.html', {'purchase_report':status})

	else:
		return render(request,'report/report.html')

def purchase_order_report(request):
	if request.method == 'GET':
		from_date = request.GET.get('from_date')
		to_date = request.GET.get('to_date')
		try:
			p_report = Purchase.objects.filter(date__range=[from_date, to_date])
		except Purchase.DoesNotExist:
			p_report = None
		return render(request, 'report/purchase_order_report.html', {'p_report':p_report})

	else:
		return render(request,'report/report.html')

def dispatch_order_report(request):
	if request.method == 'GET':
		from_date = request.GET.get('from_date')
		to_date = request.GET.get('to_date')
		try:
			p_report = Production.objects.filter(dispatched_date__range=[from_date, to_date])
		except Production.DoesNotExist:
			p_report = None
		return render(request, 'report/dispatch_report.html', {'p_report':p_report})

	else:
		return render(request,'report/report.html')

def daily_order_report(request):
	if request.method == 'GET':
		p_date = request.GET.get('p_date')
		try:
			d_report = Production.objects.filter(production_date=p_date)
		except Production.DoesNotExist:
			d_report = None
		return render(request, 'report/daily_report.html', {'d_report':d_report})

	else:
		return render(request,'report/report.html')
