from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('electronics/', views.electronics, name='electronics'),
    path('jewellery/', views.jewellery, name='jewellery'),
    path('fashion/', views.fashion, name='fashion'),
    # path('', views.dashboard, name='dashboard'),

    # path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    # path('forgotPassword/', views.forgotPassword, name='forgotPassword'),
    # path('resetpassword_validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    # path('resetPassword/', views.resetPassword, name='resetPassword'),

]
