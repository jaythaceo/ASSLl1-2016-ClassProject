from django.forms import ModelForm
from django import forms 
from models import UserAccounts
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class RegistrationForm(forms.ModelForm):
 	password2 = forms.CharField(label='Password Confirmation',
 						widget=forms.PasswordInput())

	class Meta:
		model = UserAccounts
		fields = ['email', 'password']
		widgets = {
			#changes the password input from text
			'password': forms.PasswordInput(),
		}
		exclude = ['first_name', 'last_name', 'avatar']
		#labels for forms inputs
		labels = {
			'email': _("Your Email "),
			'password': _("Enter Password")
		}
		help_texts = {
            'password': _('please enter a password of 6-15 characters'),
        }
        error_messages = {
            'password': {
            		'min_length': _("Password is to short."),
                'max_length': _("Password is to long."),
            },

        }
		
	#validates to see if passwords match
	def clean_password(self):
		pass1 = self.cleaned_data.get('password')
		pass2 = self.data.get('password2')
		if( pass1 != pass2):
			print pass1
			print pass2
			raise ValidationError(_("Password does not match. Try again"))
		else:
			print "wtf"
			#hashes the cleaned password
		clean_password = make_password(pass1)
		return clean_password

	#validates to see if email is registerd
	def clean_email(self):
		email = self.cleaned_data.get('email')
		#filters current email to those in the database and counts
		#how many, if any are alike.
		user_count = UserAccounts.objects.filter(email=email).count()
		#if there is more than one email in database similar
		#then there is an error
		if user_count > 0:
			raise forms.ValidationError("This email has already been registered. Please try again.")
		return email

