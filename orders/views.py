from django.shortcuts import render, redirect
from .models import OrderItem
from .forms import OrderForm
from cart.cart import Cart
from .tasks import order_created
from django.urls import reverse

def order_create(request):
    cart = Cart(request)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                            product=item["product"],
                                            price=item["price"],
                                            quantity=item["quantity"])
            cart.clear()
            order_created.delay(order.id)
            request.session["order_id"] = order.id
            return redirect(reverse("payment:process"))
    else:
        form = OrderForm()
    
    return render(request, "orders/order_create.html", {"form": form})


from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404
from .models import Order

@staff_member_required
def admin_order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, "admin/order_detail.html", {"order": order})