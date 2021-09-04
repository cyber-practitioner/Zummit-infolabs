from members import views
from django.urls import path,include

urlpatterns = [
    
    path('login',views.signin,name='login-page'),
]
