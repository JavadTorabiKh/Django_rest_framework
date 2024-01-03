from django.shortcuts import render



def blog_home(request):
    context = {
        'name': 'javad'
    }
    
    return render(request, "homePage/home.html", context)
