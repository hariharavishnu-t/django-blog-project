from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', required=True)
    email = forms.EmailField(label='Your Email',required=True)
    message = forms.CharField(widget=forms.Textarea, label='Your Message', required=True)