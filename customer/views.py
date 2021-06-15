from django.shortcuts import redirect, reverse, render, get_object_or_404
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db import models
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from io import BytesIO
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from django.template.loader import get_template, render_to_string
from fpdf import FPDF, HTMLMixin
from django.views.generic import ListView
from django.http import JsonResponse
import json
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .send_sms import send_sms 
from django.conf import settings


# Create your views here.
from .models import *
from .decorators import unauthenticated_user, restrict_unauthenticated_user, allowed_users



def home(request):
	context = {}
	return render(request,'customer/home.html', context)

@allowed_users(allowed_roles=['admin'])	
def adminpage(request):
	context = {}
	return render(request, 'customer/adminpage.html', context)

def how_businesslicense(request):
	context = {}
	return render(request,'customer/how_businesslicense.html',context)



def myprofile(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)
	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()
	context = {'form':form,'customer':customer}
	return render(request,'customer/myprofile.html', context)


def b_details(request):

	context = {}
	return render(request,'customer/b_details.html', context)

@restrict_unauthenticated_user
def b_license_apply(request):
	if request.user.is_authenticated:
		customer = request.user.customer 
		form = CustomerForm(instance=customer)
		if request.method == 'POST':
			warning = ""
			form = CustomerForm(request.POST, instance=customer)
			if form.is_valid():
				firststep=form.save()
				ApplicantDetails.objects.get_or_create(
					customer=customer,
					fname=customer.fname,
					mname=customer.mname,
					lname=customer.lname,
					email=customer.email,
					phonenumber=customer.phone,

					)
				messages.success(request, 'Applicant Personal Details Saved successfully')
				return redirect('secondstep')
				
	context = {'form':form, 'customer':customer}
	return render(request,'customer/b_license_apply.html', context)	


def second_step_apply(request):
	customer = request.user.customer
	applicant1 = ApplicantDetails.objects.filter(customer=customer)[0]
	applicant12 = ApplicantDetails.objects.get(id=applicant1.id)
	form = ApplicantDetailsForm(instance=applicant12)
	if request.method == 'POST':
		warning = ""
		form = ApplicantDetailsForm(request.POST, instance=applicant12)
		if form.is_valid():
			details=form.save()
			BusinessDetails.objects.get_or_create(
				customer=customer,
				email=details.email,
				tinnumber=details.plotnumber,
				managername=details.plotnumber,
				nationality=details.nationality,
				addressinfo=details.addressinfo,
				region=details.region,
				district=details.district,
				ward=details.ward,
				village=details.village,
				subvillage=details.subvillage,
				street=details.street,
				road=details.road,
				plotnumber=details.plotnumber,
				blocknumber=details.blocknumber,
				housenumber=details.housenumber,
				pobox=details.pobox,
				postalcity=details.postalcity,
				phonenumber=details.phonenumber,

				)
			messages.success(request, 'Applicant Details Saved successfully')
			return redirect('thirdstep')
	context = {'form':form, 'customer':customer}
	return render(request,'customer/second_step_apply.html', context)


def third_step_apply(request):
	customer = request.user.customer
	businessdetailsfilter = BusinessDetails.objects.filter(customer=customer)[0]
	businessdetailsID = BusinessDetails.objects.get(id=businessdetailsfilter.id)
	bussinesscustomer = businessdetailsID.customer
	form = BusinessDetailsForm(instance=businessdetailsID)
	if request.method == 'POST':
		warning = ""
		form = BusinessDetailsForm(request.POST, instance=businessdetailsID)
		if form.is_valid():
			form.save()
			PreviousLicenseDetails.objects.get_or_create(
				customer=customer,
				)
			messages.success(request, 'Business Details Saved successfully')
			return redirect('stepfive')
	context = {'form':form}
	return render(request,'customer/third_step_apply.html', context)

	
def fourth_step_apply(request):
	customer = request.user.customer
	businessdetails = BusinessDetails.objects.filter(customer=customer)[0]
	license = PreviousLicenseDetails.objects.filter(customer=customer)[0]
	licenseID = PreviousLicenseDetails.objects.get(id=license.id)

	form = PreviousLicenseDetailsForm(instance=licenseID)
	if request.method == 'POST':
		warning = ""
		form = PreviousLicenseDetailsForm(request.POST, instance=licenseID)
		if form.is_valid():
			form.save()
			#PaymentDetails.objects.get_or_create(
			#	customer=customer,
			#	businessdetails=businessdetails,
			#	amount = 43,
			#	businesscategory='Tanzanian'

			#	)
			messages.success(request, 'Your Details Saved successfully')
	context = {'form':form}
	return render(request, 'customer/fourth_step_apply.html', context)		


def fith_step_apply(request):
	customer = request.user.customer
	businesscategory = BusinessCategory.objects.all()
	if request.method == 'POST':
		category = request.POST.get('businesscategory')
		bcID = BusinessCategory.objects.filter(name=category)[0]
		bc = BusinessCategory.objects.get(id = bcID.id)
		price = bc.price
		name = bc.name
		description = bc.description

		PaymentDetails.objects.get_or_create(
			customer = customer,
			businessdetails = description,
			businesscategory = name,
			amount = price
			)
		UploadDocuments.objects.get_or_create(
			customer = customer

			)
		messages.success(request, 'Business Category selected successfully')

		return redirect('stepsix')
		
	context = {'businesscategory': businesscategory}
	return render(request,'customer/fifth_step.html', context)

def sixth_step_apply(request):
	customer = request.user.customer
	upload = UploadDocuments.objects.filter(customer=customer)[0]
	uploadID = UploadDocuments.objects.get(id=upload.id)
	form = UploadDocumentsForm(instance=uploadID)
	if request.method == 'POST':
		form = UploadDocumentsForm(request.POST, request.FILES, instance=uploadID)
		if form.is_valid():
			upload = form.save()
			upload.customer = customer
			upload.save()
			messages.success(request,'Documents Uploaded successfully')
			return redirect('waitpage')
	else:
		form = UploadDocumentsForm(instance=uploadID)


	context = {'form':form}
	return render(request, 'uploaddocuments/upload.html', context)
def waitpage(request):
	context = {}

	return render(request,'customer/waitpage.html')


def message_verification(request):
	customer = request.user.customer
	if request.method == 'POST':
		ujumbe = 'Njoo Tarehe 21 Ofisi ya Biashara Makao Makuu ya Wilaya ya Kigamboni Kuchua Leseni yako ASANTE'
		send_sms(customer.phone,ujumbe)
		messages.success(request,'Njoo Tarehe 21 Ofisi ya Biashara Makao Makuu ya Wilaya ya Kigamboni Kuchua Leseni yako ASANTE')
		return redirect('customer-dashboard')

	context = {'customer':customer}
	return render(request,'customer/message_verification.html',context)




@unauthenticated_user
def loginPage(request):
	user = authenticate()
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			query_set = Group.objects.filter(user = user).first()
			if query_set.name == 'customer': 
				return redirect('home')
			if query_set.name == 'admin':
				return redirect('admin-dashboard')
			if query_set.name == 'staff':
				return redirect('staff-dashboard')
			if 	query_set.name == 'officer':
				return redirect('')
			
		if user is None:	
			messages.info(request, 'username or password is incorrect')
		
	return render(request,'customer/signin.html')
			
			
			

def logoutUser(request):
	logout(request)
	return redirect('home')

@unauthenticated_user
def signup(request):
	form = createUserForm(request.POST or None)
	if request.method == 'POST':
		form = createUserForm(request.POST)
		if form.is_valid():	
			user = form.save()
			user.is_active = False
			user.is_customer = True
			
			user.save()
			username = form.cleaned_data.get('username')
			group = Group.objects.get(name='customer')
			user.groups.add(group)
			customer=Customer.objects.create(
				user=user,
				fname=user.first_name,
				lname=user.last_name,
				email=user.email,

				)
	


			print('oooy!')
			token = account_activation_token.make_token(user)
			user_id = urlsafe_base64_encode(force_bytes(user.id))
			url = 'localhost:8000' + reverse('confirm-email', kwargs={'user_id': user_id, 'token': token})
			message = get_template('customer/account_activation_email.html').render({'confirm_url': url})
			mail = EmailMessage('Business license Portal Account Confirmation', message, to=[user.email], from_email=settings.EMAIL_HOST_USER)
			mail.content_subtype = 'html'
			mail.send()

			messages.success(request, 'A confirmation email has been sent to your email. Please confirm to finish registration. '+ username)
			return redirect('signin')

	form = createUserForm(request.POST or None)


	return render(request,'customer/signup.html', {'form': form})

class ConfirmRegistrationView(View):
    def get(self, request, user_id, token):
        user_id = force_text(urlsafe_base64_decode(user_id))

        user = User.objects.get(pk=user_id)

        context = {
            'message': 'Registration confirmation error. Please click the resend email to generate a new confirmation email.'
        }

        if user and account_activation_token.check_token(user, token):
            user.is_active=True
            user.save()
            context['message'] = 'Registration complete. Please login'

        return render(request, 'customer/registration_complete.html', context)


def register(request):
	warning = ""
	customers = Customer.objects.all()
	form = CustomerForm()
	if request.method == 'POST':
		email = request.POST.get('email')
		if customers.filter(email=email).count() >= 1:
			warning = 'email elready exist'
			context = {'warning':warning,'form':form}
			return render(request,'customer/register.html', context)
		else:
			password1 = request.POST.get('password1')
			password2 = request.POST.get('password2')
			if password1 != password2:
				messages.warning(request, 'your passwords doesnt match')
				context = {'form':form}
				return render(request, 'customer/register.html',context)
		form = CustomerForm(request.POST or None)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('lname')
			messages.success(request, 'Account was created successfullyfor '+ user)
			return redirect('login')

	context = {'form':form}
	return render(request,'customer/register.html', context)

#first option to create PDF	
def render_to_pdf(template_src, context_dict={}):
	template = get_template(template_src)
	html  = template.render(context_dict)
	result = BytesIO()
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
	if not pdf.err:
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
	person = request.user
	customerdetails = Customer.objects.get(user=person)


data = {
	
	"company": "otieno",
	"address": "123 Street otieno",
	"city": "Vancouver",
	"state": "WA",
	"zipcode": "98663",




	"phone": "555-555-2345",
	"email": "youremail@dennisivy.com",
	"website": "dennisivy.com",
}		

class ViewPDF(View):
	def get(self, request, *args, **kwargs):

		pdf = render_to_pdf('customer/pdf_template.html', data)
		return HttpResponse(pdf, content_type='application/pdf')
class DownloadPDF(View):
	def get(self, request, *args, **kwargs):
		pdf = render_to_pdf('customer/pdf_template.html', data)
		response = HttpResponse(pdf, content_type='application/pdf')
		filename = "Invoice_%s.pdf" %("12341231")
		content = "attachment; filename='%s'" %(filename)
		response['Content-Disposition'] = content
		return response

#secon option to view PDF
def indexpdf(request):	
	context = {}
	return render(request, 'customer/indexpdf.html', context)


def myview(response):
	resp = HttpResponse(content_type='application/pdf')
	result = generate_pdf('my_template.html', file_object=resp)
	return result
class HtmlPdf(FPDF, HTMLMixin):
	pass

def print_pdf(request):
	pdf = HtmlPdf()
	pdf.add_page()
	pdf.write_html(render_to_string('pdf/example.html'))
	response = HttpResponse(pdf.output(dest='S').encode('latin-1'))
	response['Content-Type'] = 'application/pdf'
	return response


#start
def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path
#The best option to view PDF
def render_pdf_view(request, pk):
    template_path = 'pdf/pdf1.html'
    user = request.user
    customerdetails = Customer.objects.get(id=pk)
    customer = request.user.customer
    applicantdetails = ApplicantDetails.objects.filter(customer=customer)[0]
    businessdetails = BusinessDetails.objects.filter(customer=customer)[0]
    #Pre_licensedetails = PreviousLicenseDetails.get(customer=customer)
    #paymentdetails = PaymentDetails.objects.get(customer=customer)

    context = {
    "customerdetails": customerdetails,
    "applicantdetails": applicantdetails,
    "businessdetails": businessdetails,
	#"Pre_licensedetails":Pre_licensedetails,
	#"paymentdetails": paymentdetails,

     }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if u want to download use
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response





				
				
	
		


def checkout(request):
	customer=request.user.customer
    #MyModel.objects.filter(name='simple').last()
	paymentdetails = PaymentDetails.objects.filter(customer=customer)[0]
	context = {'paymentdetails':paymentdetails, 'customer':customer}
	return render(request, 'payment/checkout.html', context)

def paymentComplete(request):
	customer=request.user.customer
	body = json.loads(request.body)
	print('BODY:', body)
	paymentdetails = PaymentDetails.objects.get(id=body['productId']).last()
	#paymentdetails = PaymentDetails.objects.filter(customer=customer)[0]
	businessdetails = BusinessDetails.objects.filter(customer=customer)[0]
	Order.objects.create(
		paymentdetails=paymentdetails,
		businessdetails=businessdetails

		)
	return JsonResponse('Payment completed!', safe=False)

def simpleCheckout(request):
	return render(request, 'payment/simple_checkout.html')	



#ADMID VIEW

@allowed_users(allowed_roles=['admin'])	
def admin_dashboard(request):
	customer = request.user.customer
	form_bc = BusinessCategoryForm()
	form_staff = createUserForm()
	form_officer = createUserForm()
	context = {'form_bc': form_bc,'form_staff':form_staff,'form_officer':form_officer}
	if request.method == 'POST':
		form_bc = BusinessCategoryForm(request.POST)
		form_staff = createUserForm(request.POST)
		form_officer = createUserForm(request.POST)
		if form_bc.is_valid():
			form_bc.save()
			messages.success(request, 'Business Category created successfullyfor')
			return redirect('admin-dashboard')


		if form_staff.is_valid():
			staff = form_staff.save()
			group_staff = Group.objects.get(name='staff')
			staff.groups.add(group_staff)
			staff.is_staff = True
			staff.save()
			customer=Customer.objects.create(
				user=staff,
				fname=staff.first_name,
				lname=staff.last_name,
				email=staff.email
				)
			messages.success(request, 'Staff created successfully')
			return redirect('admin-dashboard')

		if form_officer.is_valid():
			officer = form_officer.save()
			group_officer = Group.objects.get(name='officer')
			officer.groups.add(group_officer)
			officer.save()
			customer = Customer.objects.create(
				user=officer,
				fname=officer.first_name,
				lname=officer.last_name,
				email=officer.email

				)
			messages.success(request, 'Business officer created successfully')
			return redirect('admin-dashboard')
			

		
	return render(request, 'admin/dashboard.html', context)

@allowed_users(allowed_roles=['admin'])	
def manage_bc(request):
	bc = BusinessCategory.objects.all()
	context = {'bc': bc}
	return render(request, 'admin/manage_bc.html', context)

@allowed_users(allowed_roles=['admin'])	
def delete_bc(request, pk):
	bc = BusinessCategory.objects.get(id=pk)
	if request.method == "POST":
		bc.delete()
		return redirect('managebc')
	context = {'bc': bc}
	return render(request,'admin/delete_bc.html', context)

@allowed_users(allowed_roles=['admin'])	
def	update_bc(request, pk):
	bc = BusinessCategory.objects.get(id=pk)
	form_bc = BusinessCategoryForm(instance=bc)
	context = {'form_bc': form_bc, 'bc':bc}
	if request.method == "POST":
		form_bc =  BusinessCategoryForm(request.POST, instance=bc)
		if form_bc.is_valid():
			form_bc.save()
		return redirect('managebc')

	return render(request,'admin/update_bc.html', context)


def manage_staff(request):
	
	context = {}
	return render(request, 'admin/manage_staff.html', context)



#Staff
@allowed_users(allowed_roles=['staff'])	
def staff_dashboard(request):
	context = {}
	return render(request, 'staff/dashboard.html', context)


@allowed_users(allowed_roles=['staff'])	
def new_request(request):
	c = UploadDocuments.objects.all()
	context = {'c':c}


	return render(request, 'staff/new_request.html', context)


@allowed_users(allowed_roles=['staff'])	
def delete_crequest(request, pkm):
	cr = UploadDocuments.objects.filter(id=pkm).get()
	if request.method == "POST":
		cr.delete()
		messages.success(request,'customer request has been sent to Pending')
		return redirect('new-request')

	context	= {'cr': cr}

	return render(request, 'staff/delete_request.html', context)

@allowed_users(allowed_roles=['staff'])	
def verify_request(request, pkm):
	
	person = User.objects.filter(username=pkm).get()
	customer= Customer.objects.filter(user=person).get()
	user = User.objects.filter(username=pkm).get()
	paymentdetails = PaymentDetails.objects.get(customer=customer)
	businessdetails = BusinessDetails.objects.get(customer=customer)
	
	username = user
	if request.method == 'POST':
		mail = EmailMessage('verification Message',' Your Business License have been Approved Subject To payment---->Go to your dashboard', to=[customer.email], from_email=settings.EMAIL_HOST_USER)
		mail.content_subtype = 'html'
		mail.send()
		messages.success(request,'verification email sent successfully')
		return redirect('new-request')

	context = {'customer':customer,'username':username}
	return render(request, 'staff/verify_request.html', context)





#send mail	
def instruction_mail(request, pkm):
	staff = request.user.customer
	person = User.objects.filter(username=pkm).get()
	customer= Customer.objects.filter(user=person).get()
	
	user = User.objects.filter(username=pkm).get()
	username = user
	if request.method == 'POST':

		msg = request.POST.get('message')
		mail = EmailMessage('Notification Message from Business license Portal',msg, to=[customer.email], from_email=settings.EMAIL_HOST_USER)
		mail.content_subtype = 'html'
		mail.send()


		messages.success(request, 'Notification Message has been sent to Customer ')
		return redirect('new-request')


	context = {'customer':customer,'username':username}
	return render(request, 'staff/sendmail.html', context)
	

	
	
	


def view_uploaddocuments(request, pkn):

    template_path = 'staff/view_documents.html'
    person = User.objects.filter(username=pkn).get()
    customerdetails = Customer.objects.filter(user=person).get()
    applicantdetails = ApplicantDetails.objects.filter(customer=customerdetails).get()
    businessdetails = BusinessDetails.objects.filter(customer=customerdetails).get()
    #Pre_licensedetails = PreviousLicenseDetails.get(customer=customer)
    #paymentdetails = PaymentDetails.objects.get(customer=customer)

    context = {
    "customerdetails": customerdetails,
    "applicantdetails": applicantdetails,
    "businessdetails": businessdetails,
	#"Pre_licensedetails":Pre_licensedetails,
	#"paymentdetails": paymentdetails,

     }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #if u want to download use
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@allowed_users(allowed_roles=['officer'])	
def officer_dashboard(request):

	   
	context = {}
	return render(request,'officer/dashboard.html',context)

@allowed_users(allowed_roles=['customer'])	
def customer_dashboard(request):
	customer = request.user.customer
	upload = UploadDocuments.objects.filter(customer=customer).last()
	context = {'customer': customer,'upload': upload}
	return render(request,'customer/dashboard.html', context)