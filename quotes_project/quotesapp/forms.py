from django.forms import ModelForm, CharField, DateField
from django.forms import TextInput, ModelChoiceField, ModelMultipleChoiceField, SelectMultiple
from .models import Tag, Author, Quote


class TagForm(ModelForm):

    name = CharField(
        min_length=3, max_length=25, required=True, widget=TextInput()
    )

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):

    fullname = CharField(
        min_length=3, max_length=70, required=True, widget=TextInput()
    )
    birth_date = DateField()
    birth_location = CharField(
        min_length=5, max_length=150, required=True, widget=TextInput()
    )
    description = CharField()

    class Meta:
        model = Author
        fields = ['fullname', 'birth_date', 'birth_location', 'description']


class QuoteForm(ModelForm):

    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=SelectMultiple())
    quote = CharField(
        min_length=3, max_length=255, required=True, widget=TextInput()
    )
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ["quote", "author", 'tags']
