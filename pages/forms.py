from records.models import Author, Co_advirsor, Advirsor, Student, Monograph
from django.forms import ModelForm


class AuthorForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class Co_advirsorForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class Advirsor(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class StudentForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class MonographForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"