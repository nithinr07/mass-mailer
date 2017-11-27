# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
def mail(to_send,subject,content):
	sg = sendgrid.SendGridAPIClient(apikey='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')
	from_email = Email("nithinr07@gmail.com")
	to_email = to_send.split(',')
	for i in to_email:
		mail = Mail(from_email, subject, Email(i), Content("text/plain", content))
		response = sg.client.mail.send.post(request_body=mail.get())

