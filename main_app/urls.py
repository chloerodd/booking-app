from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.About.as_view(), name='about'),
    path('services/', views.ServiceList.as_view(), name='service_list'),
    path('services/new/', views.ServiceCreate.as_view(), name="service_create"),
    path('services/<int:pk>/', views.ServiceDetail.as_view(), name='service_detail'),
    path('services/<int:pk>/update', views.ServiceUpdate.as_view(), name="service_update"),
    path('services/<int:pk>/delete', views.ServiceDelete.as_view(), name="service_delete"),
    path('reviews/', views.reviews_page, name='reviews_page'),
    path('accounts/signup/', views.Signup.as_view(), name="signup")
    
]