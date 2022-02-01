from django.shortcuts import render

# Create your views here.
def homepage(request):
    name = 'Django'
    print(name)
    return render(request, 'homepage.html', {
        'name': name
    })

def contact(request):
    return render(request, 'contact.html', {
        'email': 'contact@myapp.com'
    })