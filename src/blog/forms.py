from django import forms
from .models import Blog

# class EmailPostForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control","placeholder": "Enter your fullname"}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder": "Enter a valid email address"}))
#     to = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control","placeholder": "Enter a valid email address"}))
#     comments = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control","placeholder": "Enter comments here"}))



class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'scope', 'body', 'user')
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control","placeholder": "Title"}),
            'body': forms.Textarea(attrs={"class": "form-control","placeholder": "Message"}),
            'user': forms.HiddenInput(attrs={"class": "form-control"}),
        }
