from app_inv.views.custom_user_views import register_view
from app_inv.views.login_views import login_view
from app_inv.views.logout_view import logout_vi
from app_inv.views.profile_view import profile
from app_inv.views.password_chnage import change_password
from app_inv.views.create_catagory import add_catagory
from app_inv.views.catagory_list import catagory_list
from app_inv.views.catagory_update import catagory_update_view
from app_inv.views.delete_catagory import delete_catagory
from app_inv.views.inventory_create import inventory_create
from app_inv.views.inventory_show import Show_inventory
from app_inv.views.edit_inventory import edit_inventory
from app_inv.views.delete_inventory import delete_inventory
from app_inv.views.email_verification import verify_email
from django.urls import path


urlpatterns=[
    path('register/',register_view,name='register'),
    path('login/',login_view,name='login'),
    path('logout/',logout_vi,name='logout'),
    path ('profile/',profile,name='profile'),
    path("change_password/",change_password,name="chnage_password"),
    path('create_catagory/',add_catagory,name='add_catagory'),
    path('cat_up/<int:pk>/',catagory_update_view,name='catagory_update'),
    path('list/',catagory_list,name='catagory_list'),
    path('delete_catagory/<int:pk>/',delete_catagory,name='delete_catagory'),
    path('create_inv/',inventory_create,name='create_inventory'),
    path('edit_inv/<int:pk>/', edit_inventory,name='edit_invebtory'),
    path('delete_inv/<int:pk>/',delete_inventory,name='delete_inv'),
    path('verify/<token>/', verify_email, name='verify_email'),
    path('home/',Show_inventory,name='home'),
]