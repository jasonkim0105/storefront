from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#request -> response
#request handler, it is a called an action in node.js
def say_hello(request):
  #pull datea from db
  #transform
  #send email
  return render(request, 'hello.html', { 'name': 'Jason' })