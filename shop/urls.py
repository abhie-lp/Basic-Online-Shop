from . import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<slug:category_slug>/", views.product_list, name="product_category_list"),
    path("<int:id>/<slug:slug>/", views.product_detail, name="product_detail"),
]