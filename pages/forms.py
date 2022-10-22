from records.models import Author, Co_advirsor, Advirsor, Student, Monograph
from django.forms import ModelForm


class AuthorForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"
        