import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Brandon Lyu'
email['to'] = 'cskakarot@qq.com'
email['subject'] = 'This is an email from python lab Brandon'

email.set_content('You dare to look at me?!')


emailaddress = input('please input your email address \n')
password = input('please input your password \n')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(emailaddress,password)
	smtp.send_message(email)
	print('all done!')


