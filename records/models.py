from django.db import models

#model authors
class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    curriculum_lattes = models.URLField()
    google_scholar = models.URLField()
    reasearch_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    gitHub  = models.URLField()

    def __str__(self) -> str:
        return self.name

class Co_advirsor(models.Model):
    id_co_advisor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    curriculum_lattes = models.URLField()
    google_scholar = models.URLField()
    reasearch_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    gitHub  = models.URLField()

    def __str__(self) -> str:
        return self.name
class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    curriculum_lattes = models.URLField()
    google_scholar = models.URLField()
    reasearch_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    gitHub  = models.URLField()

    def __str__(self) -> str:
        return self.name

class Advirsor(models.Model):
    id_advisor = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    curriculum_lattes = models.URLField()
    google_scholar = models.URLField()
    reasearch_gate = models.URLField()
    linkedin = models.URLField()
    orcid = models.URLField()
    gitHub  = models.URLField()

    def __str__(self) -> str:
        return self.name

class Monograph(models.Model):
    id_monography = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    date_created = models.DateField(auto_now_add=True)
    course = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    key_words = models.CharField(max_length=255)
    date = models.DateField()
    abstract = models.TextField(max_length=2500)
    mography_link = models.URLField()

    fk_id_author = models.ForeignKey(Author, null=True, on_delete=models.SET_NULL, related_name='author')
    fk_co_advisor = models.ForeignKey(Co_advirsor, null=True, on_delete=models.SET_NULL, related_name='co_orientador')
    fk_advisor  = models.ForeignKey(Advirsor, null=True, on_delete=models.SET_NULL, related_name='orientador')

    def __str__(self) -> str:
        return self.title

