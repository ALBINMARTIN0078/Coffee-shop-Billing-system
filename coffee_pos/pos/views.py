from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import  Product, Order, OrderItem
from datetime import date
from django.db.models import Sum


def pos(request):

    products = Product.objects.all()

    if request.method == "POST":

        table = request.POST.get("table")
        payment = request.POST.get("payment")
        total = request.POST.get("total")

        order = Order.objects.create(
            table_number=table,
            payment_method=payment,
            total=total
        )

        product_ids = request.POST.getlist("product_id")
        quantities = request.POST.getlist("quantity")

        for product_id, quantity in zip(product_ids, quantities):
            product = Product.objects.get(id=product_id)
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=int(quantity)
            )

        return redirect("receipt", order_id=order.id)

    return render(request,"pos.html",{"products":products})


def receipt(request, order_id):

    order = Order.objects.get(id=order_id)

    return render(request,"receipt.html",{"order":order})


def report(request):

    orders = Order.objects.all()

    total_sales = sum(order.total for order in orders)

    return render(request,"report.html",{
        "orders":orders,
        "total_sales":total_sales
    })