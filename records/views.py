from django.shortcuts import render
from pages.forms import AuthorForms, Co_advirsorForms, MonographForms, StudentForms


def registerOfAuthors(request):
    if request.method == "POST":
        form = AuthorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = AuthorForms()
            return render(request, 'registerauthors.html', {'form': form})
    else:
        form = AuthorForms()
            
    return render(request, 'registerauthors.html', {'form': form})

def registerOfCoAdvisor(request):
    if request.method == "POST":
        form = Co_advirsorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = AuthorForms()
            return render(request, 'registerauthors.html', {'form': form})
    else:
        form = Co_advirsorForms()
            
    return render(request, 'registercoadvisor.html', {'form': form})


def registerOfStudents(request):
    if request.method == "POST":
        form = StudentForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = StudentForms()
            return render(request, 'registerstudents.html', {'form': form})
    else:
        form = StudentForms()
            
    return render(request, 'registercoadvisor.html', {'form': form})

def registerOfmonographs(request):
    if request.method == "POST":
        form = MonographForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = MonographForms()
            return render(request, 'registermonograph.html', {'form': form})
    else:
        form = MonographForms()
            
    return render(request, 'registercoadvisor.html', {'form': form})




