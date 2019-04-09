from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

app_name = 'users'

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html',
                                                redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('account/', user_views.account, name='account'),

    # Password reset paths
    path('account/reset-password/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),

    path('account/reset-password/done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),

    path('account/reset-password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('account/reset-password/complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
