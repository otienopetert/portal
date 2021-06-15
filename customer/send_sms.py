from twilio.rest import Client



def send_sms(phone,ujumbe):
	account_sid = 'AC284ee5d6f2b47953a6b563b945b28055'
	auth_token = 'e0265d4cf5459da96ca903e5abf0c784'
	client = Client(account_sid, auth_token)

	message = client.messages \
	    .create(
	         body=ujumbe,
	         from_='+12059004096',
	         to='{}'.format(phone) # receiver
	     )

	print(message.sid)