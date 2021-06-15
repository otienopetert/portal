from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
	SEX_CATEGORY = (

		('Male','Male'),
		('Female','Female'),

		)
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	fname = models.CharField(max_length=200, null=True)
	mname = models.CharField(max_length=200, null=True)
	lname = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	dob = models.CharField(max_length=200, null=True)
	gender = models.CharField(max_length=200, null=True, choices=SEX_CATEGORY)
	profile_pic = models.ImageField(default="user.png", null=True, blank=True)
	logo = models.ImageField(default="layout_set_logo.png", null=True, blank=True, editable=False)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):
	    return str(self.user)

class ApplicantDetails(models.Model):

	N_CATEGORY = (

		('Tanzanian','Tanzanian'),
        ('Foreigner','Foreigner'),

		)

	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	fname = models.CharField(max_length=200, null=True)
	mname = models.CharField(max_length=200, null=True)
	lname = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	nationality = models.CharField(max_length=200, null=True, choices=N_CATEGORY)
	addressinfo = models.CharField(max_length=200, null=True, blank=False)
	region = models.CharField(max_length=200, null=True)
	district = models.CharField(max_length=200, null=True)
	ward = models.CharField(max_length=200, null=True)
	village = models.CharField(max_length=200, null=True)
	subvillage = models.CharField(max_length=200, null=True)
	street = models.CharField(max_length=200, null=True)
	road = models.CharField(max_length=200, null=True)
	plotnumber = models.CharField(max_length=200, null=True)
	blocknumber = models.CharField(max_length=200, null=True)
	housenumber = models.CharField(max_length=200, null=True)
	pobox = models.CharField(max_length=200, null=True)
	postalcity = models.CharField(max_length=200, null=True)
	phonenumber = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.fname)



class BusinessDetails(models.Model):

	N_CATEGORY = (

	('Tanzanian','Tanzanian'),
    ('Foreigner','Foreigner'),

	)

	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	tinnumber = models.CharField(max_length=200, null=True)
	managername = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	nationality = models.CharField(max_length=200, null=True, choices=N_CATEGORY)
	addressinfo = models.CharField(max_length=200, null=True, blank=False)
	region = models.CharField(max_length=200, null=True)
	district = models.CharField(max_length=200, null=True)
	ward = models.CharField(max_length=200, null=True)
	village = models.CharField(max_length=200, null=True)
	subvillage = models.CharField(max_length=200, null=True)
	street = models.CharField(max_length=200, null=True)
	road = models.CharField(max_length=200, null=True)
	plotnumber = models.CharField(max_length=200, null=True)
	blocknumber = models.CharField(max_length=200, null=True)
	housenumber = models.CharField(max_length=200, null=True)
	pobox = models.CharField(max_length=200, null=True)
	postalcity = models.CharField(max_length=200, null=True)
	phonenumber = models.CharField(max_length=200, null=True)

	def __str__(self):
		return str(self.customer)



class PreviousLicenseDetails(models.Model):
	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	licensenumber = models.CharField(max_length=200, null=True)
	date_issue = models.CharField(max_length=200, null=True)
	expiredate = models.CharField(max_length=200, null=True)
	feepaid = models.FloatField(max_length=200, null=True)
		
	def __str__(self):
		return self.licensenumber


class PaymentDetails(models.Model):
	
	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	businessdetails = models.CharField(max_length=200, null=True)
	businesscategory = models.CharField(max_length=200, null=True)
	amount = models.FloatField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.customer


class Order(models.Model):
	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	paymentdetails = models.ForeignKey(PaymentDetails, null = True, on_delete= models.SET_NULL, blank=True)
	businessdetails = models.ForeignKey(BusinessDetails, null = True, on_delete= models.SET_NULL, blank=True)
	def __str__(self):
		return self.id


class BusinessCategory(models.Model):
	customer = models.ForeignKey(Customer, null = True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(max_length=200, null=True)
	description = models.CharField(max_length=200, null=True)
	def __str__(self):
		return self.name

class UploadDocuments(models.Model):
	customer = models.ForeignKey(Customer, null = True, on_delete= models.SET_NULL, blank=True)
	citizenship = models.FileField(upload_to='uploaddocuments/pdf/', null=True)
	rent = models.FileField(upload_to='uploaddocuments/pdf/', null=True)
	tax = models.FileField(upload_to='uploaddocuments/pdf/', null=True)
	authority = models.FileField(upload_to='uploaddocuments/pdf/',null=True)
	def __str__(self):
		return self.customer


#class RequestLicense(models.Model):
	

