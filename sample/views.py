from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'sample/index.html')
def electronics(request):
    return render(request, 'sample/electronics.html')
def fashion(request):
    return render(request, 'sample/fashion.html')
def jewellery(request):
    return render(request, 'sample/jewellery.html')