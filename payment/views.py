from django.shortcuts import render, get_object_or_404, redirect
import braintree
from orders.models import Order

def payment_process(request):
    order_id = request.session.get("order_id")
    order = get_object_or_404(Order, id=order_id)

    if request.method == "POST":
        nonce = request.POST.get("payment_method_nonce", None)
        result = braintree.Transaction.sale({
            "amount": f"{order.get_total_cost():.2f}",
            "payment_method_nonce": nonce,
            "options": {
                "submit_for_settlement": True,
            }
        })
        if result.is_success:
            order.paid = True
            order.braintree_id = result.transaction.id
            order.save()
            return redirect("payment:done")
        else:
            return redirect("payment:canceled")
    else:
        client_token = braintree.ClientToken.generate()
        return render(request, "payment/process.html", {"order": order, "client_token": client_token})
    

def payment_done(request):
    return render(request, "payment/done.html")


def payment_canceled(request):
    return render(request, "payment/canceled.html")