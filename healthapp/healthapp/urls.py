from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from doctor import views
from rest_framework.authtoken.views import obtain_auth_token
#obtain_auth_token فيو بيعمل aceess للمودل حق الtokens 
from django.contrib.auth.views import LoginView , LogoutView
#from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('doctor.urls')),
   # path('api/',include('healthapp.urls',namespace='api')),
    #path('api-token-auth/',obtain_auth_token),
   # path('doctor/',include('doctor.urls',namespace='doctor'))
    #path('login/',LoginView.as_view(templete_name='اسم صفحة الlogin من الفلتر'),name='login'),
   # path('logout/',LogoutView.as_view(),name='logout'),
  #  path('Signup/',include('doctor.urls')),
    path('PatientSignUp/',views.create_new_paient),
    path('doctorList/',views.doctors_list),
    path('PatientAllAppointments/',views.Show_my_Appointments),
    path('bookAppointment/',views.BookAppointment),
    path('DoctorSignUp/',views.create_new_Doctor),
    path('DoctorInserAppointment/',views.createNewAppoinment),
    path('vacc/',views.getVacc),
    path('vacc/<str:pk>/',views.getVaccByID)

]
