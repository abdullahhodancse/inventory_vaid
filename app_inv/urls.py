from app_inv.views.custom_user_views import register_view
from app_inv.views.login_views import login_view
from app_inv.views.logout_view import logout_vi
from app_inv.views.profile_view import profile
from app_inv.views.password_chnage import change_password
from django.urls import path


urlpatterns=[
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_vi,name='logout'),
    path ('profile/',profile,name='profile'),
    path("change_password/",change_password,name="chnage_password"),
]