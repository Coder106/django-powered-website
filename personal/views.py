from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'personal/home.html')


def contact(request):
    return render(request, 'personal/basic.html', {'content':['If you would like to contact me email me at','codercoder106@gmail.com']})

