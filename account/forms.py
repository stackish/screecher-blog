from django import forms
from django.forms import Widget,EmailInput,TextInput,PasswordInput
from django.contrib.auth.forms import  UserCreationForm,UserChangeForm
from .models import AccountUser
from django.utils.translation import  gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm

#UserCreationForm
class AccountCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model=AccountUser
		fields=['first_name','last_name','email','username','password1','password2']
		widgets={

		#'username':TextInput(attrs={'class':'form-control','placeholder':'Username','required':True,}),
		#'email':EmailInput(attrs={'class':'form-control','placeholder':'Email Address','required':True,}),
		'first_name':TextInput(attrs={'autofocus':True}),
		'last_name':TextInput(attrs={'class':'form-control'}),
		}
		
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'placeholder':'First name','maxlength':30})	
		self.fields['last_name'].widget.attrs.update({'placeholder':'Last name','maxlength':30})
		self.fields['email'].widget.attrs.update({'placeholder':'Email Address','maxlength':100})
		self.fields['username'].widget.attrs.update({'placeholder':'Username','maxlength':30})
		self.fields['password1'].widget.attrs.update({'placeholder':'*********','maxlength':30})
		self.fields['password2'].widget.attrs.update({'placeholder':'*********','maxlength':30})



	def clean_email(self,*args,**kwargs):
		email=self.cleaned_data.get('email')
		email=email.lower()
		return email
		
	def clean_username(self,*args,**kwargs):
		username=self.cleaned_data.get('username')
		return username.lower()
		
		
		
	
	#def __init__(self, *args, **kwargs):
		#super().__init__(*args, **kwargs)
	
		#self.fields['username'].widget.attrs.update({'class': 'form-control','id':'formGroupExampleInput','type':'text'})

		#self.fields['password1'].widget.attrs.update({'class': 'form-control','id':'exampleInputPassword1','type':'password'})
		#self.fields['password2'].widget.attrs.update({'class': 'form-control','id':'exampleInputPassword2','type':'password'})
		
		
	
				
				
				
				
	
#UserChangeForm		
		
class AccountChangeForm(UserChangeForm):
	class Meta(UserChangeForm):
		model=AccountUser
		fields=['username','first_name','last_name']
		
		
	def clean_email(self,*args,**kwargs):
		email=self.cleaned_data.get('email')
		email=email.lower()
		return email
		
		
		
		
#Login form		
class LoginForm(AuthenticationForm):
	class Meta:
		model=AccountUser
		fields=['email','password']


	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['username'].widget.attrs.update({'placeholder':'Email Address','maxlength':100})
		self.fields['password'].widget.attrs.update({'placeholder':'**********','maxlength':30})
		

		
	def clean_email(self,*args,**kwargs):
		email=self.cleaned_data.get('email')
		email=email.lower()
		return email
		
		
	def clean_username(self,*args,**kwargs):
		username=self.cleaned_data.get('username')
		
		
		return username.lower()
			
					
		
			
			
	
			
			
			
	
			
			
		
			
		
		
		
			
		
			
		