from django import forms

class NewSearchForm(forms.Form):
    title = forms.CharField(label="",
            widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'})
            )
    
class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="",required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Title of Encyclopedia'})
                                )
    content = forms.CharField(label="", required=True, 
                widget=forms.Textarea(attrs={'placeholder': 'Content'}), max_length=600)    