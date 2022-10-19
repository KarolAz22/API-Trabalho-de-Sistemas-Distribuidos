from django.shortcuts import render
from records.models import Monograph
# Create your views here.
def home(request):
    return render(request, 'home.html')

def search(request):
    select = request.POST.get('select')
    result = request.POST.get('search')
    if(select == 'title'):
        lista = Monograph.objects.filter(title__icontains = result)
        monograph = lista[0]
    if(select == 'course'):
        lista = Monograph.objects.filter(course__icontains = result)
        monograph = lista[0]
    if(select == 'university'):
        lista = Monograph.objects.filter(university__icontains = result)
        monograph = lista[0]
    if(select == 'keywords'):
        lista = Monograph.objects.filter(key_words__icontains = result)
        monograph = lista[0]
    if(select == 'abstract'):
        lista = Monograph.objects.filter(abstract__icontains = result)
        monograph = lista[0]
    if(select == 'author'):
        lista = Monograph.objects.filter(fk_id_author__icontains = result)
        monograph = lista[0]
    if(select == 'advisor'):
        lista = Monograph.objects.filter(fk_advisor__icontains = result)
        monograph = lista[0]
    if(select == 'coadvisor'):
        lista = Monograph.objects.filter(fk_co_advisor__icontains = result)
        monograph = lista[0]

    print(monograph)
    return render(request, 'home.html', {'monograph': monograph})