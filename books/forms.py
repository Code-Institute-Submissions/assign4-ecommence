from django import forms
from .models import Book, Author

class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','published','ISBN','length','authors','quotes','desc','cost')


class AuthorForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=('first_name','last_name','biography')