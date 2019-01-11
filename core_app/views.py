from django.shortcuts import render


def main(request):
    return render(request, 'core_app/main.html')


def products(request):
    return render(request, 'core_app/products.html')


def contacts(request):
    return render(request, 'core_app/contacts.html')


