from django import forms

class NewSearchForm(forms.Form):
    title = forms.CharField(label="",
            widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'})
            )