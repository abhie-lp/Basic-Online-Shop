from . import views
from django.urls import path

app_name = "orders"

urlpatterns = [
    path("create/", views.order_create, name="order_create"),
]