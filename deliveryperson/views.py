from django.shortcuts import render

# Create your views here.


def delivery(request):
	return render(request,'待送訂單.html')