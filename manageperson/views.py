from django.shortcuts import render

# Create your views here.
def manage(request):
	return render(request,'總公司.html')

def report(request):
	return render(request,'銷售報表.html')

def cusanalysis(request):
	return render(request,'顧客分析.html')

def cuscluster(request):
	return render(request,'顧客分群.html')
