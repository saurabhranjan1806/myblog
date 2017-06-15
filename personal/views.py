from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'personal/home.html')

def contact(request):
	return render(request, 'personal/contact.html', {'content': ['if you want to contact then go to my email id', 'saurabhranjan1806@gmail.com']})