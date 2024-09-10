from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Sepeda',
        'price' : '2000000',
        'quantity' : '10',
        'description': 'sepeda roda dua, cocok untuk pemula'
    }

    return render(request, "main.html", context)
