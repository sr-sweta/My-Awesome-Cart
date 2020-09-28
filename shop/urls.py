from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='ShopHome'),
    path('about/',views.about,name='AboutUs'),
    path('tracker/',views.tracker,name='TrackingStatus'),
    path('contact/',views.contact,name='ContactUs'),
    path('search/',views.search,name='Search'),
    path('products/<int:myid>',views.productView,name='ProductView'),#<int:myid> is used for unique identification of a prod
    path('checkout/',views.checkout,name='Checkout'),
    path("handlerequest/", views.handlerequest, name="HandleRequest"),

]