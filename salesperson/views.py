from django.shortcuts import render

# Create your views here.

def sales(request):
	return render(request,'銷售人員.html')

def newmember(request):
	return render(request,'新增會員.html')

def newsales(request):
	return render(request,'加入購買資訊.html')

def checkinventory(request):
	return render(request,'存貨查詢系統.html')
