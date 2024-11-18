from django.urls import path
from . import views

urlpatterns = [
  
   path('',views.home, name='home'),
   path('fruit/<int:shop_id>/',views.fruit, name='fruit'),
   path('user_login',views.user_login, name='user_login'),
   path('user_logout',views.user_logout, name='user_logout'),
   path('editfruit/<int:shop_id>/',views.editfruit, name='editfruit'),

   


]
