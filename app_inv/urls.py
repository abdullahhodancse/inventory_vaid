from django.urls import path
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
from app_inv.views.middleware_email import middle
from app_inv.views.passwors_reset_com import complete
from django.contrib.auth import views as auth_views
from app_inv.views.pass_reset_view import CustomPasswordResetView
from django.urls import reverse_lazy


urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_vi, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_password/', change_password, name='change_password'),
    path('create_catagory/', add_catagory, name='add_catagory'),
    path('cat_up/<int:pk>/', catagory_update_view, name='catagory_update'),
    path('list/', catagory_list, name='catagory_list'),
    path('delete_catagory/<int:pk>/', delete_catagory, name='delete_catagory'),
    path('create_inv/', inventory_create, name='create_inventory'),
    path('edit_inv/<int:pk>/', edit_inventory, name='edit_inventory'),
    path('delete_inv/<int:pk>/', delete_inventory, name='delete_inv'),
    path('email_verification/',middle,name='email_verification'),
    path('complete/',complete,name='complete'),
    path('home/', Show_inventory, name='home'),

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', success_url=reverse_lazy('password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    
    
    path('<str:token>/', verify_email, name='verify_email'),


    
]

   
