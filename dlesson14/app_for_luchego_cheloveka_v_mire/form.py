from django import forms

class Blog_form(forms.Form):
    name = forms.CharField(required=True)
    title = forms.CharField(required=True)
    text = forms.CharField(required=True, widget=forms.Textarea)
    quantity_of_likes = forms.IntegerField(required=True)

