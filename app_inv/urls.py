from app_inv.views.custom_user_views import register_view
from app_inv.views.login_views import login_view
from app_inv.views.logout_view import logout_vi
from django.urls import path


urlpatterns=[
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_vi,name='logout'),
]