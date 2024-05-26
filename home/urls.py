from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static
from .views import streamlit_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', views.home_view,name="home"),
    path('login', views.loginuser,name="login"),
    path('logout',views.logoutuser,name="logout"),
    path('register',views.register,name="register"),
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('streamlit/', streamlit_view, name='streamlit_view'),
    path('sales-data/', views.sales_data, name='sales_data'),
    path('api/salesdata/', views.get_sales_data, name='sales_data'),
    path('get_current_username/', views.get_current_username, name='get_current_username'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/get_current_username/', views.get_current_username, name='get_current_username'),
    path('streamlit-app/', views.streamlit_app, name='streamlit_app')
    # path('api-token-auth/', views.obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)