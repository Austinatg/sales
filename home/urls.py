from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from .views import streamlit_view

urlpatterns = [
    path('', views.home_view,name="home"),
    path('login', views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('register',views.register,name="register"),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('streamlit/', streamlit_view, name='streamlit_view'),
    path('sales-data/', views.sales_data, name='sales_data'),
    path('api/salesdata/', views.get_sales_data, name='sales_data'),
    path('get_current_username/', views.get_current_username, name='get_current_username')
    # path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)