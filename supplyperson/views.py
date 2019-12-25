from django.shortcuts import render

# Create your views here.

def supply(request):
	return render(request,'庫存查詢系統.html')