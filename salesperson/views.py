from django.shortcuts import render
from home.models import Customer,Order
from django.http import HttpResponse

# Create your views here.

def sales(request):
	return render(request,'銷售人員.html')

def newmember(request):
	return render(request,'新增會員.html')

def newsales(request):
	return render(request,'加入購買資訊.html')

def checkinventory(request):
	return render(request,'存貨查詢系統.html')

def new_member(request):
	if 'id' in request.POST:
		cus_id = request.POST['id']
	if 'name' in request.POST:
		cus_name = request.POST['name']
	if 'telnum' in request.POST:
		cus_tel =  request.POST['telnum']
	if 'address' in request.POST:
		cus_addr = request.POST['address']
	if 'age' in request.POST:
		cus_age = request.POST['age']
	if 'email' in request.POST:
		cus_email = request.POST['email']
	if 'family_mem' in request.POST:
		cus_family_mem = request.POST['family_mem']
	if 'income' in request.POST:
		cus_income = request.POST['income']
	if 'date' in request.POST:
		cus_date = request.POST['date']

	member = Customer(customer_id = cus_id,customer_name = cus_name,customer_tel = cus_tel,customer_address = cus_addr,customer_age = cus_age,email = cus_email,num_familymembers = cus_family_mem,register_date = cus_date, monthly_income = cus_income)
	member.save()

	return render(request,'新增成功.html') 

#def new_purchase(request):
#	if '型號' in request.POST:

