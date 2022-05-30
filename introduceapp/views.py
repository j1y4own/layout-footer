from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'account.html')

def bootstrap(request):
    return render(request, 'bootstrap.html')

def grid(request):
    return render(request, 'grid.html')

def myschedule(request):
    return render(request, 'myschedule.html')

def test(request):
    return render(request, 'test.html')

def footer(request):
    return render(request, 'footer.html')