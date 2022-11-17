from rest_framework.routers import DefaultRouter
from .views import RegisterView,ChangePasswordView,UpdateProfileView,MyObtainTokenPairView,StartGameView,UpdateGameView,RetriveGameView,ListGameView,DestroyUserView
from django.urls import path,include
from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('token/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('update_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('delete_user/<int:pk>/',DestroyUserView.as_view(),name='delete_user'),
    path('start_game',StartGameView.as_view(),name='start_game'),
    path('get_board/<int:pk>/',RetriveGameView.as_view(),name='get_board'),
    path('update_board/<int:pk>/',UpdateGameView.as_view(),name='update_board'),
    path('list_games',ListGameView.as_view(),name='list_game'),
    
]
