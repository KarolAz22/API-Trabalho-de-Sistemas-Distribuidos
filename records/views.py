from django.shortcuts import render
from pages.forms import AuthorForms, AdvisorForms , Co_advisorForms, MonographForms, StudentForms


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
        form = Co_advisorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = Co_advisorForms()
            return render(request, 'registerauthors.html', {'form': form})
    else:
        form = Co_advisorForms()
            
    return render(request, 'registercoadvisor.html', {'form': form})

def registerOfAdvisor(request):
    if request.method == "POST":
        form = AdvisorForms(request.POST)
        if form.is_valid():
            post = form.save()
            post.save()
            form = AdvisorForms()
            return render(request, 'registerauthors.html', {'form': form})
    else:
        form = AdvisorForms()
            
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




