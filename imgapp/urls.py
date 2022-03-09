from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("add_product", views.add_product, name="add_product"),
    path("show_products", views.show_products, name="show_products"),
    path("edit_product_details/<int:id>", views.edit_product_details, name="edit_product_details"),
    path('editpage/<int:id>',views.editpage,name='editpage'),
    path("delete/<int:id>",views.delete,name='delete')
]