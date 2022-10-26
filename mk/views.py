from django.shortcuts import render
from .lr import predict_price

# Create your views here.

def home(request):
    return render(request, 'mk/home.html')

def result(request):
    if request.method =='GET':
        sqft = request.GET['sqft']
        bath = request.GET['bath']
        bhk = request.GET['bhk']
        location = request.GET['Location']
        print(f'answer is {predict_price(location,sqft,bath,bhk)}')
    return render(request, 'mk/result.html', {'price': round(predict_price(location,sqft,bath,bhk),2)})
