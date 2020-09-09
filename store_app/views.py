from django.shortcuts import render, redirect


PRODUCTS = [
    {"id": 1001, "name": "wireless mouse", "price": "36.99"},
    {"id": 1002, "name": "headset", "price": "48.50"},
    {"id": 1003, "name": "keyboard", "price": "22.99"},
    {"id": 1004, "name": "camera", "price": "399.95"},
]

def index(request):
    context = {"products": PRODUCTS}
    return render(request, "index.html", context)

def add_to_cart(request, p_id):
    print(p_id)
    print(request.POST)
    if "cart" in request.session:
        request.session["cart"].append({
            "name": request.POST["name"], 
            "price":  request.POST["price"]
        })
        request.session.modified = True
    else:
        request.session["cart"] = [{
            "name": request.POST["name"], 
            "price":  request.POST["price"]
        }]
    return redirect("/")

def view_cart(request):
    return render(request, "cart.html")