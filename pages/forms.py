from records.models import Author, Co_advisor, Advisor, Student, Monograph
from django.forms import ModelForm


class AuthorForms(ModelForm):
    class Meta: 
        model = Author
        fields = "__all__"

class Co_advisorForms(ModelForm):
    class Meta: 
        model = Co_advisor
        fields = "__all__"

class AdvisorForms(ModelForm):
    class Meta: 
        model = Advisor
        fields = "__all__"

class StudentForms(ModelForm):
    class Meta: 
        model = Student
        fields = "__all__"

class MonographForms(ModelForm):
    class Meta: 
        model = Monograph
        fields = "__all__"