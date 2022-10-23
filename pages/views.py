from django.http import Http404
from django.shortcuts import render
from records.models import Monograph, Author, Advirsor, Co_advirsor
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
            advisor = Advirsor.objects.get(name=result)
            monograph = Monograph.objects.filter(fk_advisor = advisor)
        except:
            monograph = []
    elif(select == 'coadvisor'):
        try:
            coadvisor = Co_advirsor.objects.get(name=result)
            monograph = Monograph.objects.filter(fk_co_advisor = coadvisor)
        except:
            monograph = []
            
    if(len(monograph) > 0):
        return render(request, 'home.html', {'monographs': monograph})
    else:
        return render(request, 'home.html', {'message': "Nenhum resultado encontrado"})

def details(request, pk):
    print("Primary Key {}".format(pk))
    try:
        monographs = Monograph.objects.filter(id_monography=pk)
        print(monographs.values)
    except monographs.DoesNotExist:
        raise Http404("Monograph do not exists")
    
    return render(request, 'monograph.html', {'monographs': monographs})

