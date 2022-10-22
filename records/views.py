from django.shortcuts import render
from pages.forms import AuthorForms


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

def registerOfCoAuthors():
    pass

def registerOfStudents():
    pass

def registerOfmonographs():
    pass



