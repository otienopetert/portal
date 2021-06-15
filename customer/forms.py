from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ApplicantDetailsForm(ModelForm):
	class Meta:
		model = ApplicantDetails
		fields = '__all__'
		exclude = ['customer']

class BusinessDetailsForm(ModelForm):
	class Meta:
		model = BusinessDetails
		fields = '__all__'
		exclude = ['customer']

class PreviousLicenseDetailsForm(ModelForm):
	class Meta:
		model = PreviousLicenseDetails
		fields = '__all__'
		exclude = ['customer']
class PaymentDetailsForm(ModelForm):
	class Meta:
		model = PaymentDetails
		fields = '__all__'
		exclude = ['customer']

class BusinessCategoryForm(ModelForm):
	class Meta:
		model = BusinessCategory
		fields = '__all__'
		exclude = ['customer']


class UploadDocumentsForm(ModelForm):
	class Meta:
		model = UploadDocuments
		fields = '__all__'
		exclude = ['customer']