from django import forms

class LeadForm(forms.Form):
    # Define your lead capture form fields here
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # Add more fields as needed


class LeadCaptureForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(max_length=100, label='Your Email')
    company = forms.CharField(max_length=100, label='Company Name')
    phone = forms.CharField(max_length=20, label='Phone Number')
    message = forms.CharField(widget=forms.Textarea, label='Message')
