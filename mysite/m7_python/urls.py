from django.urls import path,include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
               path('', views.indexView, name='home'),
               path('login/', LoginView.as_view(next_page='dashboard'), name='login_url'),
               path('logout/', LogoutView.as_view(next_page='home'), name='logout_url'),
               path('register/', views.registerView, name='register_url'),
               path('register_tipo/', views.register_tipoView, name='register_tipo_url'),
               path('dashboard/', views.dashboardView, name='dashboard'),
               path('update_profile/', views.profile, name='update_profile'),
               path('new_inmueble/', views.new_inmuebleView, name='new_inmueble_url'),
               path('update_inmueble/', views.inmuebles_update, name='update_inmueble_url'),
               path('eliminar_inmueble/', views.eliminar_inmueble, name='eliminar_inmueble'),
               path('acerca/', views.acerca, name='acerca'),
               path('cuenta/', views.bienvenido, name='cuenta'),
               path('contacto/', views.contacto, name='contacto'),
               path('exito/', views.exito, name='exito'),
               ]