from django.forms import ModelForm, ModelChoiceField, CharField, TextInput, Textarea, Select
from .models import Author, Tag, Quote
from .utils import get_mongodb


# db = get_mongodb()

def authors_list():
    db = get_mongodb()
    authors = []
    base = db.authors.find()
    for author in base:
        authors.append(author['fullname'])
    return authors


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, required=True, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorName'}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorBornAt'}))
    born_location = CharField(max_length=150, widget=TextInput(attrs={'class': 'form-control', 'id': 'AuthorBornIn'}))
    description = CharField(widget=Textarea(attrs={'class': 'form-control', 'id': 'AuthorDescription'}))


    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(ModelForm):
    quote = CharField(required=True, widget=TextInput(attrs={'class': 'form-control', 'id': 'QuoteText'}))
    author = ModelChoiceField(queryset = Author.objects.all(), widget=Select(attrs={'class': 'form-control', 'id': 'QuoteAuthor'}))
    # author = CharField( widget=TextInput(attrs={'class': 'form-control', 'id': 'QuoteAuthor'}))


    class Meta:
        model = Quote
        fields = ('quote', 'tags', 'author')


class TagForm(ModelForm):
    name = CharField(widget=TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Tag
        fields = ('name',)


