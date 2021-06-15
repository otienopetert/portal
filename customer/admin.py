from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(ApplicantDetails)
admin.site.register(BusinessDetails)
admin.site.register(PreviousLicenseDetails)
admin.site.register(PaymentDetails)


