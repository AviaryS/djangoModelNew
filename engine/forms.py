from django import forms


class PostForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea, label='Контент')
    isPublish = forms.BooleanField(label='Опубликовать', required=False)
    date = forms.CharField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}))