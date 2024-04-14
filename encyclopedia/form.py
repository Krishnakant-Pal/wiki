from django import forms

# search form
class NewSearchForm(forms.Form):
    title = forms.CharField(label="",
            widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'})
            )
# New entry form
class NewEntryForm(forms.Form):
    new_title = forms.CharField(label="",required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Title of Encyclopedia'})
                                )
    content = forms.CharField(label="", required=True, 
                widget=forms.Textarea(attrs={'placeholder': 'Content'}), max_length=600)    
    
# new entry form
class EditEntryForm(forms.Form):
    title = forms.CharField(label="",required=True, 
                                widget= forms.HiddenInput
                                (attrs={'class':'col-sm-12','style':'bottom:1rem'}))
                                

    content = forms.CharField(label="", required=True, 
                widget=forms.Textarea(attrs={'placeholder': 'Content'}), max_length=600)  