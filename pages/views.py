from django.http import Http404
from django.shortcuts import render
from records.models import Monograph, Author, Advisor, Co_advisor, Student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    select = request.POST.get('select')
    result = request.POST.get('search')

    if(select == 'title'):
        monograph = Monograph.objects.filter(title__icontains = result)
    elif(select == 'course'):
        monograph = Monograph.objects.filter(course__icontains = result)
    elif(select == 'university'):
        monograph = Monograph.objects.filter(university__icontains = result)
    elif(select == 'keywords'):
        monograph = Monograph.objects.filter(key_words__icontains = result)
    elif(select == 'abstract'):
        monograph = Monograph.objects.filter(abstract__icontains = result)
    elif(select == 'author'):
        try:
            author = Author.objects.get(name=result)
            monograph = Monograph.objects.filter(fk_id_author = author.id_author)
        except:
            monograph = []
    elif(select == 'advisor'):
        try:
            advisor = Advisor.objects.get(name=result)
            monograph = Monograph.objects.filter(fk_advisor = advisor)
        except:
            monograph = []
    elif(select == 'coadvisor'):
        try:
            coadvisor = Co_advisor.objects.get(name=result)
            monograph = Monograph.objects.filter(fk_co_advisor = coadvisor)
        except:
            monograph = []
            
    if(len(monograph) > 0):
        return render(request, 'home.html', {'monographs': monograph})
    else:
        return render(request, 'home.html', {'message': "Nenhum resultado encontrado"})

def details(request, pk):
    try:
        monographs = Monograph.objects.filter(id_monography=pk)
    except monographs.DoesNotExist:
        raise Http404("Monograph do not exists")
    
    return render(request, 'monograph.html', {'monographs': monographs})

def delete(request, pk):
    try: 
        Monograph.objects.filter(id_monography=pk).delete()
    except:
        raise Http404("Unable to delete data")
    return render(request, 'home.html')

def getAllUsers():
    authors = Author.objects.all()
    advisors = Advisor.objects.all()
    co_advisors = Co_advisor.objects.all()
    students = Student.objects.all()
    context = {
        'authors': authors,
        'advisors': advisors,
        'co_advisors': co_advisors,
        'students': students,
        }
    return context

def getAllMonographs():
    monographs = Monograph.objects.all()
    context = {
        'monographs': monographs
    }
    return context

def showAllMonographs(request):
    monographs = getAllMonographs()
    return render(request, 'monographs.html', context=monographs)

def showAllUsers(request):
    users = getAllUsers()
    return render(request, 'users.html', context=users)