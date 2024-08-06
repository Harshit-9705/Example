from django.core.mail import send_mail,EmailMessage
from django.conf import settings

def send_mail_client():
    subject = "JUST CHECKING CODE"
    message = "This is spam message if you click onn this your pc is hacked now!!!"
    from_email = settings.EMAIL_HOST_USER
    reci = ['bhargavbaldaniya777@gmail.com']
    send_mail(subject,message,from_email,reci)


def send_mail_attch(subject,message,rece,file_path):
    mail = EmailMessage(subject=subject,body=message,from_email=settings.EMAIL_HOST_USER,to = rece)

    mail.attach_file(file_path)

    mail.send()
    