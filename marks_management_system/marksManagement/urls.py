from django.urls import path
from . import views
  
urlpatterns = [
    # path('', include('home.urls')),
   path('',views.login,name='login'),
   path('facultyLogin',views.loginAsFaculty ,name='loginFaculty'),
   path('stdashboard',views.dashboard,name='dashboard'),
   path('reportCard/<str:usersub>',views.reportCard,name='reportCard'),
   
   path('facultydashboard',views.facultydashboard,name='facultydashboard'),
]

# /<str:user>/