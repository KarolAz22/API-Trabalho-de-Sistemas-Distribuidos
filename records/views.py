from django.http import Http404
from django.shortcuts import get_object_or_404, render
from pages.forms import AuthorForms, AdvisorForms , Co_advisorForms, MonographForms, StudentForms
from .models import Author ,Advisor ,Co_advisor, Student, Monograph
from pages.views import getAllMonographs, getAllUsers



def registerOfAuthors(request):
    if request.method == "GET":
        form = AuthorForms()
        return render(request, 'registerauthor.html', {'form': form})
    elif request.method == "POST":
        form = AuthorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)     
        else:
            form = AuthorForms()
            return render(request, 'registerauthor.html', {'form': form})

def registerOfCoAdvisor(request):
    if request.method == "GET":
        form = Co_advisorForms()
        return render(request, 'registercoadvisor.html', {'form': form})
    elif request.method == "POST":
        form = Co_advisorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            users = getAllUsers()
            return render(request, 'users.html', context=users)    
        else:
            form = Co_advisorForms()
            return render(request, 'registercoadvisor.html', {'form': form})

def registerOfAdvisor(request):
    if request.method == "GET":
        form = AdvisorForms()
        return render(request, 'registeradvisor.html',{'form': form})
    elif request.method == "POST":
        form = AdvisorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)    
        else:
            form = AdvisorForms()
            return render(request, 'registeradvisor.html', {'form': form})


def registerOfStudent(request):
    if request.method == "GET":
        form = StudentForms
        return render(request, 'registerstudents.html', {'form': form})
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)    
        else:
            form = StudentForms() 
            return render(request, 'registerstudents.html', {'form': form})

def registerOfmonographs(request):
    if request.method == "GET":
        form = MonographForms()
        return render(request, 'registermonograph.html', {'form': form})
    if request.method == "POST":
        form = MonographForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = MonographForms()
            context = getAllMonographs()
            return render(request, 'monographs.html', context=context)
        else:
            message = "Author present in another monograph"
            form = MonographForms()
            return render(request, 'registermonograph.html', {'form': form, 'message': message})

def deleteAuthor(request,pk):
    try:
        Author.objects.filter(id_author=pk).delete()
    except:
        raise Http404("Unable to delete author")
    context = getAllUsers()
    return render(request, 'users.html', context=context)    

def deleteAdvisor(request,pk):
    try:
        Advisor.objects.filter(id_advisor=pk).delete()
    except:
        raise Http404("Unable to delete advisor")
    context = getAllUsers()
    return render(request, 'users.html', context=context)     

def deleteCoadvisor(request,pk):
    try:
        Co_advisor.objects.filter(id_co_advisor=pk).delete()
    except:
        raise Http404("Unable to delete advisor")
    context = getAllUsers()
    return render(request, 'users.html', context=context)     

def deleteStudent(request,pk):
    try:
        Student.objects.filter(id_student=pk).delete()
    except:
        raise Http404("Unable to delete advisor")
    context = getAllUsers()
    return render(request, 'users.html', context=context)     

def alterAuthor(request, pk):    
    author = get_object_or_404(Author,id_author=pk)
    form = AuthorForms(instance=author)
    if request.method=="POST":
        form = AuthorForms(request.POST, instance=author)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)
    elif request.method=="GET":
        return render(request, 'alterauthor.html', {'form': form, 'author': author})

def alterAdvisor(request, pk):
    advisor = get_object_or_404(Advisor,id_advisor=pk)
    form = AdvisorForms(instance=advisor)
    if request.method=="POST":
        form = AdvisorForms(request.POST, instance=advisor)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)
    elif request.method=="GET":
        return render(request, 'alteradvisor.html', {'form': form, 'advisor': advisor})

def alterCoAdvisor(request, pk):
    co_advisor = get_object_or_404(Co_advisor,id_co_advisor=pk)
    form = AdvisorForms(instance=co_advisor)
    if request.method=="POST":
        form = Co_advisorForms(request.POST, instance=co_advisor)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            context = getAllUsers()
            return render(request, 'users.html', context=context)
    elif request.method=="GET":
        return render(request, 'altercoadvisor.html', {'form': form, 'coadvisor': co_advisor})

def alterStudent(request, pk):
    student = get_object_or_404(Student,id_student=pk)
    form = StudentForms(instance=student)
    if request.method=="POST":
        form = StudentForms(request.POST, instance=student)
        post = form.save(commit=False)
        post.save()
        context = getAllUsers()
        return render(request, 'users.html', context=context)
    elif request.method=="GET":
        return render(request, 'alterstudent.html', {'form': form, 'student': student})
