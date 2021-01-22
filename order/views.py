from django.shortcuts import render, redirect
from .models import Order
from .forms import OrderForm
from django.core.exceptions import ObjectDoesNotExist


def all_orders(request):
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})


# Create your views here.

def order_by_id(request, id=0):
    order_by_id = Order.objects.get(id=id)
    return render(request, 'order/order_by_id.html', {'title': "Order by ID", "order_by_id": order_by_id})

def order_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = OrderForm()
            return render(request, 'order/order_form_add.html', {'form': form})
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(instance=order)
            return render(request, 'order/order_form.html', {'form': form})
    else:
        if id == 0:
            form = OrderForm(request.POST)
        else:
            order = Order.objects.get(id=id)
            form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
        return redirect('orders')



def order_update(request):
    # def book_update(request, book_id=0, name, description, author, count):
    # if name:
    #     Book.objects.get(id=book_id).name = name
    # if description:
    #     Book.objects.get(id=book_id).description = description
    # if author:
    #     Book.objects.get(id=book_id).author = author
    # if count:
    #     Book.objects.get(id=book_id).count = count
    # Book.save()
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})


def order_delete(request, id=0):
    order = Order.objects.get(id=id)
    order.delete()
    # Book.save()
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})
