from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # path('', views.home, name="home"),

    path('sign_up/', views.sign_up, name="sign_up"),
    path('sign_in/', views.sign_in, name="sign_in"),
    path('logout/', views.logout, name="logout"),


    # path('admit_card/<int:applicant_id>/', views.admit_card, name="admit_card"),
]