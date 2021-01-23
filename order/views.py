from django.shortcuts import render, redirect
from .forms import OrderForm
from .models import Order
from rest_framework import viewsets, generics, permissions
from .serializers import OrderSerializer, OrderDetailSerializer, OrderListSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication



class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderDetailSerializer

class OrderListView(generics.ListAPIView):
    serializer_class = OrderListSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAdminUser, IsAuthenticated, )

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('id')
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


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

    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})


def order_delete(request, id=0):
    order = Order.objects.get(id=id)
    order.delete()
    # Book.save()
    orders = list(Order.objects.all())
    return render(request, 'order/all_orders.html', {'title': "All orders", "orders": orders})
