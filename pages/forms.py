from records.models import Author, Co_advirsor, Advirsor, Student, Monograph
from django.forms import ModelForm


class AuthorForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class Co_advirsorForms(ModelForm):
    class Meta: 
        model = Co_advirsor
        fields = "__all__"

class Advirsor(ModelForm):
    class Meta: 
        model = Advirsor
        fields = "__all__"

class StudentForms(ModelForm):
    class Meta: 
        model = Student
        fields = "__all__"

class MonographForms(ModelForm):
    class Meta: 
        model = Monograph
        fields = "__all__"