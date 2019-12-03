from django.urls import path
from . import views

app_name = 'pets'

urlpatterns = [
    # path('', views.home, name="home"),

    path('dashboard/', views.dashboard, name="dashboard"),
    path('add_pet/', views.add_pet, name="add_pet"),
    path('edit_pet/<int:id>', views.edit_pet, name="edit_pet"),
    path('pet_profile/<int:id>', views.pet_profile, name="pet_profile"),
    path('appointments', views.appointmens , name="appointments"),
    path('new_appointment', views.new_appointment, name="new_appointment"),
    path('prescription/<int:id>', views.prescription, name="prescription"),
    path('products',  views.products, name="products"),
    path('add_forum', views.add_forum, name="add_forum"),
    path('forums', views.forums, name="forums"),
    path('forum/<int:id>', views.forum_details, name="forum_details"),

    # path('admit_card/<int:applicant_id>/', views.admit_card, name="admit_card"),
]