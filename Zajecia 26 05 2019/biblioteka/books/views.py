from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from books.models import Book


# def hello_world(request, name=""):
#     if name:
#         text = f"Hello {name}"
#     else:
#         text = "Hello world"
#     return HttpResponse(text)
#
#
# def lista_ksiazek(request):
#     ksiazki = [{'title': "Nic"}, {'title': "1984"}]
#     output = ""
#     for ksiazka in ksiazki:
#         output += ksiazka['title'] + "<br>"
#     return HttpResponse(output)


# ---------------------------------------------------------
def books_list(request):
    books = Book.objects.all()
    return render(
        request=request,
        template_name="index.html",
        context={'books': books}
    )


def book_detiles(request, id):
    book = Book.objects.get(id=id)
    return render(
        request=request,
        template_name="details.html",
        context={'book': book}
    )


def login(request):
    return render(
        request=request,
        template_name="login.html"
    )
