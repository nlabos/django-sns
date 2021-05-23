from django import forms

class PostForm(forms.Form):
    content = forms.CharField(max_length=5000, 
    widget=forms.Textarea(attrs={'class': 'form-control'}))
    image = forms.ImageField(label='画像', required=False)

