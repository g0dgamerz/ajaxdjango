from django import forms

class AjaxForm(forms.Form):
	email=forms.EmailField()
	name=forms.CharField(max_length=120)

	def clean_email(self):
		email = self.cleaned_data.get("email")
		if email == "abc@gmail.com":
			raise forms.ValidationError("this is not valid")
		return email