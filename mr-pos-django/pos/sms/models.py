from django.db import models
from pos.g_model import TimeStampMixin
from settings.models import Customer
from django.core.mail import EmailMessage
from datetime import datetime 
from django.utils.translation import gettext as _

# image upload for employee
def get_upload_directory(instance, filename):
    # Generate the upload directory based on the current date
    return f"files/email/{datetime.now().strftime('%Y/%m/%d')}"


class SendSms(TimeStampMixin):
    customer = models.ForeignKey(Customer, on_delete= models.CASCADE)
    message = models.CharField(max_length=160, blank=True, null=True)
                        
    class Meta:
        verbose_name = _('Sms')
        verbose_name_plural = _('Sms')
      
    def __str__(self) -> str:
        return f"{self.id}"
    
class SendEmail(TimeStampMixin):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255,blank=True, null=True)
    message = models.CharField(max_length=2500, blank=True, null=True)
    file = models.FileField(blank=True, null=True, upload_to=get_upload_directory)
                        
    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Email')
      
    def __str__(self) -> str:
        return f"{self.id}"

############ send email with attachment  start ########################
 
# from django.core.mail import EmailMessage

# # create an email message object
# message = EmailMessage(
#     subject='Subject of the email',
#     body='Body of the email',
#     from_email='sender@example.com',
#     to=['recipient1@example.com', 'recipient2@example.com'],
# )

# # attach a file to the email message
# message.attach_file('/path/to/attachment.pdf')

# # send the email with the attachment
# message.send()

# To send an email with an attachment in Django, you will need to use the EmailMessage class from the django.core.mail module. This class allows you to define the subject, sender, recipient, and body of the email, as well as attach files to the email.

# Here is an example of how you might use the EmailMessage class to send an email with an attachment in Django:

# Copy code
# from django.core.mail import EmailMessage

# email = EmailMessage(
#     subject='Email with Attachment',
#     body='Here is the body of the email',
#     from_email='sender@example.com',
#     to=['recipient@example.com'],
# )

# # Attach the file to the email
# email.attach_file('path/to/file.pdf')

# # Send the email
# email.send()
# In this example, we create an instance of the EmailMessage class, specify the subject, body, sender, and recipient of the email, and attach a file to the email using the attach_file() method. Finally, we send the email using the send() method.

# It's important to note that this example assumes that you have already configured Django to use a specific email backend for sending emails. If you haven't done this, you can read the Django documentation on email configuration to learn how to do it.

############ send email with attachment  end ########################




    