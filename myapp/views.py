from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def view1(request):
	s="<h1>this is 1st resopnse"
	return HttpResponse(s)

def view2(request):
	s="<h1>this is 2nd resopnse"
	return HttpResponse(s)
