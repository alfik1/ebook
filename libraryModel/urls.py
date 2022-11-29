from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views


urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    
    path('', views.GetEbooks.as_view(), name='all' ),
    path('create-ebook', views.CreateEbook.as_view(),name='create' ),
    path('update-ebook', views.UpdateEbook.as_view(),name='update' ),
    path('delete-ebook/<int:id>', views.DeleteEbook.as_view(),name='delete' ),
    path('search-ebook', views.SearchEbook.as_view()),

] 