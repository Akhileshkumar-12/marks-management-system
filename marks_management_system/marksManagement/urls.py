from django.urls import path
from . import views
  
urlpatterns = [
    # path('', include('home.urls')),
   path('',views.login,name='login'),
   path('stdashboard',views.dashboard,name='dashboard'),
   path('reportCard',views.reportCard,name='reportCard'),
   
   path('facultydashboard',views.facultydashboard,name='facultydashboard'),
]
