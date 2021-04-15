from django.urls import path
from . import views
  
urlpatterns = [
    # path('', include('home.urls')),

   path('',views.dashboard,name='dashboard'),
   path('reportCard',views.reportCard,name='reportCard'),
   path('login',views.login,name='login'),

]
