from django import forms
 
class AccountForm(forms.Form):
    userId = forms.CharField(max_length=100, label='AOJ ID ')
	
class SubmitForm(forms.Form):
	languages = (
		('', '言語を選択'),
		('0', 'C++'),
		('1', 'Python3'),
	)
	language = forms.ChoiceField(widget=forms.Select, choices=languages)
	#sourceCode = forms.TextField()