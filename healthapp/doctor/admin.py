from django.contrib import admin
from .models import *
admin.site.register(Patient)
admin.site.register(doctors)
admin.site.register(DoctorInfo)
admin.site.register(Vaccine)
#admin.site.register(VaccineLocations)
admin.site.register(BookedAppoiments)
admin.site.register(DoctorsAppointment)
admin.site.register(VaccineLocations)

# Register your models here.
