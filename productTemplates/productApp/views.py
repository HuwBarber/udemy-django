from django.shortcuts import render

def index(request):
    return render(request, "productApp/index.html")

def electronics(request):
    products={
        "product1": "Mac",
        "product2": "iPhone",
        "product3": "Windows"
    }
    return render(request, "productApp/products.html", products)

def toys(request):
    products={
        "product1": "Jack in the Box",
        "product2": "Truck",
        "product3": "Doll"
    }
    return render(request, "productApp/products.html", products)

def shoes(request):
    products={
        "product1": "Adidas",
        "product2": "Nike",
        "product3": "New Balance"
    }
    return render(request, "productApp/products.html", products)
