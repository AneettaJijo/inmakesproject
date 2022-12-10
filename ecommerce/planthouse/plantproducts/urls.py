from . import views
from django.urls import path, include
app_name='plantproducts'
urlpatterns=[
    path('',views.allcategory,name='AllProdC'),
    path('<slug:c_slug>/',views.allcategory,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.prodcategory,name="ProdCat")

]