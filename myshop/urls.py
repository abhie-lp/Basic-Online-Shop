from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("cart/", include("cart.urls", namespace="cart")),
    path("payment/", include("payment.urls", namespace="payment")),
    path("", include("shop.urls", namespace="shop")),
    path("coupons/", include("coupons.urls", namespace="coupons")),
    path("orders/", include("orders.urls", namespace="orders")),
]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
