from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('blogs', views.blogs, name="blogs"),
    path('blogs/<int:id>', views.blog_details, name="blog_details"),
    path('team', views.team, name="team"),

    # path('admit_card/<int:applicant_id>/', views.admit_card, name="admit_card"),
]