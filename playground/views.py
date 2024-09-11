from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response
#request handler, it is a called an action in node.js

def calculate():
  x = 1
  y = 1
  return x

def say_hello(request):
  #pull datea from db
  #transform
  #send email
  x = calculate()
  return render(request, 'hello.html', { 'name': 'Jason' })