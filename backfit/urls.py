from django.urls import path
from . import views
urlpatterns = [
    path('adminlogin/', views.admin_login, name='admin_login'),
    # path('admindash/', views.admindash, name="admindash")

]
