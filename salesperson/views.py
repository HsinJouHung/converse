from django.shortcuts import render
from home.models import Customer,Product,Store,Order
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

def new_order(request):
	if 'date' in request.POST:
		order_date = request.POST['date']
	if 'pay_method' in request.POST:
		order_method = request.POST['pay_method']
	if 'discount_rate' in request.POST:
		order_discount = request.POST['discount_rate']
	if 'member_id' in request.POST:
		cid = request.POST['member_id']
		order_member = Customer.objects.get(customer_id = cid)
	if 'product_id' in request.POST:
		pid = request.POST['product_id']
		order_product = Product.objects.get(product_id = pid)
	if 'store_id' in request.POST:
		sid = request.POST['store_id']
		order_store = Store.objects.get(store_id = sid)
	if 'shoe_size' in request.POST:
		order_size = request.POST['shoe_size']
		

	o = Order(order_date = order_date,order_method = order_method,discount_rate = order_discount,customer_id = order_member,product_id = order_product,store_id = order_store,size = order_size)
	o.save()

	return render(request,'新增成功.html')