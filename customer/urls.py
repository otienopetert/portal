from django.urls import path
#from django.urls import include, re_path
from django.contrib.auth import views as auth_views

from .import views



urlpatterns = [
   path('', views.home, name="home"),
   #admin
   path('admin-dashboard/', views.admin_dashboard, name="admin-dashboard"),
   path('manage-business-category/', views.manage_bc, name="managebc"),
   path('delete-business-category/<str:pk>/', views.delete_bc, name="delete_bc"),
   path('update-business-category/<str:pk>/', views.update_bc, name="update_bc"),
   #staff
   path('staff-dashboard/', views.staff_dashboard, name="staff-dashboard"),
   path('new-request/', views.new_request, name="new-request"),
   path('Delete-Customer-Request/<str:pkm>/', views.delete_crequest, name="delete_crequest"),
   path('instruction-mail/<str:pkm>/', views.instruction_mail, name="instruction-mail"),
   path('verify-request/<str:pkm>/', views.verify_request, name="verify-request"),
   path('manage-staff/', views.manage_staff, name="manage-staff"),
   
   
   #officer
   path('officer-dashboard/', views.officer_dashboard, name="officer-dashboard"),
   #customer
   path('customer-dashboard/', views.customer_dashboard, name="customer-dashboard"),
   path('message-verification/', views.message_verification, name="message-verification"),
   path('how-businesslicense/', views.how_businesslicense, name="how-businesslicense"),
   



   
   path('myprofile/', views.myprofile, name="myprofile"),
   path('signup/', views.signup, name="signup"),
   path('business-license-details/', views.b_details, name="products"),
   path('business-licence-apply/', views.b_license_apply, name="stepone"),
   #signin&signout&register
   path('signin/', views.loginPage, name="signin"),
   path('logout/', views.logoutUser, name="logout"),
   path('register/', views.register, name="register"),
   #application steps
   path('second-step-apply/', views.second_step_apply, name="secondstep"),
   path('third-step-apply/', views.third_step_apply, name="thirdstep"),
   path('fourth-step-apply/', views.fourth_step_apply, name="fourthstep"),
   path('fith-step-apply/', views.fith_step_apply, name="stepfive"),
   path('sixth-step-apply/', views.sixth_step_apply, name="stepsix"),
   path('waitpage/', views.waitpage, name="waitpage"),
   #reset password
   path('reset_password/', auth_views.PasswordResetView.as_view(template_name="customer/password_reset.html"),
   name="reset_password"),
   path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="customer/password_reset_sent.html"),
   name="password_reset_done"),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="customer/password_reset_form.html"),
   name="password_reset_confirm"),
   path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="customer/password_reset_done.html"),
   name="password_reset_complete"),
   #html to pdf
   path('indexpdf/', views.indexpdf, name="indexpdf"),
   path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
   path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),
   #staff view uploaded documents
   path('view-uploaddocuments/<str:pkn>/', views.view_uploaddocuments, name="view_uploaddocuments"),
   path('test-view/<str:pk>/', views.render_pdf_view, name="test-view"),
   path('checkout/', views.checkout, name="checkout"),
   path('complete/', views.paymentComplete, name="complete"),
   path('simple-checkout/', views.simpleCheckout, name="simple-checkout"),
   #change password
   path('password_change/', auth_views.PasswordChangeView.as_view(template_name="passwordchange/change-password.html"), name="password_change"),
   path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name="passwordchange/change-password-done.html"), name="password_change_done"),
   

   path('confirm-email/<str:user_id>/<str:token>/', views.ConfirmRegistrationView.as_view(), name='confirm-email'),

]
