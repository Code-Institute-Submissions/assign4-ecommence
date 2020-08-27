from django import forms
from .models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'authors', 'published', 'ISBN', 'length',
                  'quotes', 'desc', 'cost', 'image')


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name',  'biography', 'image')


# Search Form
class SearchForm(forms.Form):
    # seach by book title
    title = forms.CharField(max_length=100, required=False)
    # search by author title
    authors = forms.ModelChoiceField(queryset=Author.objects.all(),
                                     required=False)
