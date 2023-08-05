from django.urls import path
from .import views
urlpatterns = [
    path('',views.login),
    path('Home',views.login),
    path('Login',views.login,name="login"),
    path('Logout',views.logout,name="Logout"),
    path('Signup',views.signup,name="Signup"),
    path("Contact",views.Contact, name = "Contact"),
    path('index',views.index,name ="loginpage"),
    path('gro',views.gro)

]
