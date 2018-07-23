from django import forms
 
class AccountForm(forms.Form):
    userId = forms.CharField(max_length=100, label='AOJ ID ')