from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306244955',
        'name': 'Muhammad Faizi Ismady Supardjo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
