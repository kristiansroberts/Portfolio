from django.forms import ModelForm
from portfolio.models import ContactSubmission  

class ContactSubmissionForm(ModelForm):
    class Meta:
        model = ContactSubmission
        fields = ['name', 'email', 'message']