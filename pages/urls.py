from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='#home'),
    path('returns',views.returns,name='#returns'),
    # path('delivery',views.delivery,name='#delivery'),
    path('cart',views.cart,name='cart')
    
]